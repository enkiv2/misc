#!/usr/bin/env zsh

available_filters=(mat randomColorScene randomColorFrame zoomIn zoomOut randomZoom fliph flipv mirrorh mirrorv kaleid randomFilter)
enabled_filters=(mat)
minimum_clip_length=0
parallelism=20
resolution="640:480"
fps=24
cps=4

cmdname=$0
pid=$$
dir=~/.fake-mvgen/${pid}

DEBUGLEVEL=0

function dprint() {
	if [[ $1 -le $DEBUGLEVEL ]] ; then
		shift
		echo "$@" > /dev/stderr
	fi
}

function dshell() {
	d=$1 ; shift
	dprint $d "Running shell command: " "$@"
	"$@"
}

function help() {
	dprint 0  "Usage: $cmdname audiofile outfile [options...] source_directory [source_directory...]"
	dprint 0  "Options:"
	dprint 0  "  Filter options:"
	for filter in $available_filters ; do 
		def="(default $([[ ${enabled_filters[(ie)$filter]} -le ${#enabled_filters} ]] && echo "ON" || echo "OFF"))"
		dprint 0  "    +filter_$filter\tUse $filter filter $def"
		dprint 0  "    -filter_$filter\tDo not use $filter filter $def"
	done
	dprint 0 "    -nofilters\tDo not use any filters"
	dprint 0 "  Verbosity options:"
	dprint 0 "    -v\tVerbosity level 1"
	dprint 0 "    -vv\tVerbosity level 2"
	dprint 0 "    -vvv\tVerbosity level 3"
	dprint 0 "  Misc options:"
	dprint 0 "    -m length\tSpecify minimum clip length in seconds (default 1/cps = $((1.0/cps)))"
	dprint 0 "    -p threads\tSpecify parallelism (default: $parallelism)"
	dprint 0 "    -r res\tSpecify output resolution (default: $resolution)"
	dprint 0 "    -fps rate\tSpecify output frame rate (default: $fps)"
	dprint 0 "    -cps rate\tSpecify number of source clips per second of output (default: $cps)"
	exit 1
}


function getLength() {
	(mplayer -vo null -ao null -identify -frames 0 "$@" | (grep '^ID_LENGTH=[0-9\.]*$' || echo 0) | sed 's/^ID_LENGTH*=//' )2>/dev/null
}
function getFPS() {
	(mplayer -vo null -ao null -identify -frames 0 "$@" | (grep '^ID_VIDEO_FPS=[0-9\.]*$' || echo 0) | sed 's/^ID_VIDEO_FPS*=//;s/\..*$//' )2>/dev/null
}
function convertLength() {
	len=$1
	this_fps=$2 
	if [[ $this_fps -lt $fps ]] ; then
		len=$(( (len*fps)/this_fps ))
	fi
	echo $len
}
function convertLengthInverse() {
	len=$1
	this_fps=$2
	if [[ $this_fps -lt $fps ]] ; then
		len=$(( (len*this_fps)/fps ))
	fi
	echo $len
}
function getLengthAdjusted() {
	convertLength $(getLength "$@") $(getFPS "$@")
}
function floor() {
	echo "$@" | cut -d. -f 1
}
function ceil() {
	floor $(($1+0.5))
}
function skip() {
	i=0
	while read x ; do
		if [[ $i -eq $1 ]] ; then
			echo "$x"
			i=0
		else
			i=$((i+1))
		fi
	done
}
function dup() {
	while read x ; do
		i=0
		while [[ $i -lt $1 ]] ; do
			cp "$x" "${x}_${i}.jpg"
			echo "${x}_${i}.jpg"
			i=$((i+1))
		done
	done
}
function randomHex() {
	for i in {1..9} {a..f} ; do
		echo $i
	done | shuf -n 1
}
function randomColor() {
	red=$(randomHex)$(randomHex)
	green=$(randomHex)$(randomHex)
	blue=$(randomHex)$(randomHex)
	echo "#${red}${green}${blue}"
}

function convertCompositeHelper() {
	item="$1" ; shift
	rm -f ${item}-2.jpeg
	convert "$item" "png32:${item}.png"
	dshell 2 convert "$item" "$@" "png32:${item}-2.png"
	[[ -e ${item}-2.png ]] && {
		dshell 2 composite ${item}-2.png ${item}.png ${item}-3.png
		dshell 2 convert ${item}-3.png ${item}-2.jpeg
		[[ -e ${item}-2.jpeg ]] && mv ${item}{-2.jpeg,}
		rm -f ${item}.png ${item}-2.png ${item}-3.png
	}
}

function convertCompositeFilterHelper() {
	func=$1
	desc=$2
	i=0
	for item in $(cat $dir/cliplist) ; do
		( 
			setopt SH_WORD_SPLIT
			convertCompositeHelper $item $($func)
			unsetopt SH_WORD_SPLIT
		)  &
		i=$((i+1))
		if [[ $i -gt $parallelism ]] ; then
			dprint 2 "Waiting for $desc to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done ; wait
}

function mirrorh() {
	echo "-flop -matte -channel A +level 0,50% +channel"
}

function mirrorv() {
	echo "-flip -matte -channel A +level 0,50% +channel"
}

function filter_mirrorh() {
	dprint 2 "horizontal mirror filter"
	convertCompositeFilterHelper "mirrorh" "mirrorh"
}

function filter_mirrorv() {
	dprint 2 "vertical mirror filter"
	convertCompositeFilterHelper "mirrorv" "mirrorv"
}

function filter_kaleid() {
	dprint 2 "kaleidoscope filter"
	convertCompositeFilterHelper "mirrorh" "mirrorh"
	convertCompositeFilterHelper "mirrorv" "mirrorv"
}
	

function convertHelper() {
	item="$1" ; shift
	rm -f ${item}-2.jpeg
	dprint 2 "Running shell command: " convert "$item" "$@" "${item}-2.jpeg"
	convert "$item" "$@" "${item}-2.jpeg"
	[[ -e ${item}-2.jpeg ]] && mv ${item}{-2.jpeg,}
}

function convertFilterHelper() {
	func=$1
	desc=$2
	i=0
	for item in $(cat $dir/cliplist) ; do
		( 
			setopt SH_WORD_SPLIT
			convertHelper $item $($func)
			unsetopt SH_WORD_SPLIT
		)  &
		i=$((i+1))
		if [[ $i -gt $parallelism ]] ; then
			dprint 2 "Waiting for $desc to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done ; wait
}

function mat() {
	res=$(echo $resolution | sed 's/:/x/')
	echo "-resize $res -background black -gravity center -extent $res"
}

function filter_mat() {
	dprint 2 "mat filter"
	convertFilterHelper "mat" "mat"
}

function fliph() {
	echo "-flop"
}

function filter_fliph() {
	dprint 2 "horizontal flip filter"
	convertFilterHelper "fliph" "fliph"
}

function flipv() {
	echo "-flip"
}

function filter_flipv() {
	dprint 2 "vertical flip filter"
	convertFilterHelper "flipv" "flipv"
}

function rcs() {
	color=$1
	[[ -z "$color" ]] && color="$(randomColor)"
	echo "-fill $color -tint 110"
}

function filter_randomColorScene() {
	# random color scene
	color="$(randomColor)"
	dprint 2 "Coloring scene: $color"
	convertFilterHelper "rcs $color" "color correction"
}
function filter_randomColorFrame() {
	# random color scene
	dprint 2 "Coloring scene: $color"
	convertFilterHelper rcs "color correction"
}
function calculateDelta() {
	# currently: 1/3rd of the smaller coordinate
	sz=$1
	if [[ $sz -lt $2 ]]; then
		sz=$2
	fi
	echo $(floor $((sz/3)))
	
}
function zoomFilterHelper() {
	cmd=$1
	count=$(wc -l < $dir/cliplist)
	xsz=$(echo $resolution | cut -d: -f 1)
	ysz=$(echo $resolution | cut -d: -f 2)
	delta=$(calculateDelta $xsz $ysz)
	dprint 2 "Calculated delta: $delta"
	dprint 2 "Count: $count"
	delta=$((delta/count))
	dprint 2 "Delta: $delta"
	j=1
	for item in $($cmd $dir/cliplist | uniq) ; do
		dprint 2 "i*delta: $((j*delta))"
		( 
			convertHelper $item -crop $(( xsz-(2*j*delta) ))x$(( ysz-(2*j*delta) ))+$((j*delta))+$((j*delta)) +repage 
		) &
		j=$((j+1))
		if [[ $i -gt $parallelism ]] ; then
			dprint 2 "Waiting for zoom to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done; wait
}
function filter_zoomIn() {
	dprint 2 "Zooming in on scene"
	zoomFilterHelper cat
}
function filter_zoomOut() {
	dprint 2 "Zooming out on scene"
	zoomFilterHelper tac
}
function filter_randomZoom() {
	if [[ $((RANDOM%2)) -gt 0 ]] ; then
		filter_zoomIn
	else
		filter_zoomOut
	fi
}

function filter_randomFilter() {
	num_filters=${#available_filters}
	i=$((RANDOM%num_filters+1))
	filter=${available_filters[i]}
	filter_$filter
}

function applyFilters() {
	pushd $1
	for filter in $enabled_filters ; do
		dprint 1 "Filtering with $filter"
		filter_$filter
	done
	popd
}

function process_args() {
	[[ $# -lt 3 ]] && help
	[[ "$1" == "-h" ]] && help

	export audiofile=$1
	export outfile=$2
	shift ; shift
	
	while `echo $1 | grep -q '^[-+]'` ; do
		opt=$1
		shift
		if [[ "$opt" == "--" ]] ; then 
			continue
		fi
		dprint 2 "Found option $opt"
		if `echo "$opt" | grep -q '^[-+]filter_'` ; then	
			filter=$(echo $opt | cut -d_ -f 2-)
			dprint 2 "Filter name: $filter"
			if `echo $opt | grep -q '^+filter_'` ; then
				if [[ ${available_filters[(ie)$filter]} -le ${#available_filters} ]] ; then
					if [[ ${enabled_filters[(ie)$filter]} -le ${#enabled_filters} ]] ; then
						dprint 2 "Filter already enabled: $filter"
					else
						enabled_filters+=($filter)
					fi
				else
					echo "Unknown filter: $filter"
					help
				fi
			elif `echo $opt | grep -q '^-filter_'`; then
				if [[ ${available_filters[(ie)$filter]} -le ${#available_filters} ]] ; then
					if [[ ${enabled_filters[(ie)$filter]} -le ${#enabled_filters} ]]  ; then
						filters_to_remove=($filter)
						enabled_filters=(${enabled_filters:|filters_to_remove})
					else
						dprint 2 "Filter already disabled: $filter"
					fi
				else
					dprint 0 "Unknown filter: $filter"
					help
				fi
			fi
		elif [[ "$opt" == "-v" ]] ; then
			export DEBUGLEVEL=1
		elif [[ "$opt" == "-vv" ]] ; then
			export DEBUGLEVEL=2
		elif [[ "$opt" == "-vvv" ]] ; then
			export DEBUGLEVEL=3
		elif [[ "$opt" == "-nofilters" ]] ; then
			export enabled_filters=()
		elif [[ "$opt" == "-m" ]] ; then
			export minimum_clip_length=$1
			shift
		elif [[ "$opt" == "-p" ]] ; then
			export parallelism=$1
			shift
		elif [[ "$opt" == "-r" ]] ; then
			export resolution=$1
			shift
		elif [[ "$opt" == "-fps" ]] ; then
			export fps=$1
			shift
		elif [[ "$opt" == "-cps" ]] ; then
			export cps=$1
			shift
		else
			dprint 0 "Unknown option: $opt"
			help
		fi
	done
	dprint 1 "Enabled filters: $enabled_filters"
	dprint 2 "DEBUGLEVEL: $DEBUGLEVEL"
	export enabled_filters
#  exit
	initial_setup "$@"
}

function print_summary() {
	dprint 0 "================================================================================"
	dprint 0 "= Audio file: \"$audiofile\""
	dprint 0 "= Target clip length: $clip_length seconds ($cps clips per second)"
	dprint 0 "= Minimum source clip length: $minimum_clip_length seconds"
	dprint 0 "= Source directories: "
	for i in "$@" ; do
		dprint 0 "= \t$i"
	done
	dprint 0 "= $(wc -l $dir/sources) sources"
  dprint 0 "= Enabled filters: $enabled_filters"
	dprint 0 "= Temp dir: $dir"
	dprint 0 "= Number of threads: $parallelism"
	dprint 0 "= Output resolution: $resolution"
	dprint 0 "=   FPS:             $fps"
	dprint 0 "=   CPS:             $cps"
	dprint 0 "================================================================================"
	if [[ $(wc -l $dir/sources | cut -d\  -f 1) -lt 1 ]] ; then
		dprint 0 "ERROR: No suitable sources; exiting."
		exit 1
	fi
}

function print_if_long_enough() {
			dprint 2 "File: $1" 
			l=$(getLength "$1")
			dprint 2 "Clip length: $l" 
			l=$(floor $((l*1000)))
			if [[ $l -gt $ml ]] ; then
				echo "$1"
				dprint 0 -e ".\c"
			else
				dprint 0 -e "-\c"
			fi

}

function get_file_line() {
	head -n $1 "$2" | tail -n 1
}

function remove_short_sources_r() {
	num_sources=$1
	i=$2
	while [[ $i -lt num_sources ]] ; do
		x="$(get_file_line $i $dir/sources)"
		print_if_long_enough "$x"
		i=$((i+1))
	done
}

function remove_short_sources_parallel() {
	num_sources=$1
	num_jobs=$parallelism
	if [[ $num_jobs -gt $num_sources ]]; then
		num_jobs=$num_sources
	fi
	sources_per_job=$((num_sources/num_jobs))
	dprint 0 "Checking length of $num_sources sources in $num_jobs batches of $sources_per_job sources each."
	for i in {0..$((num_jobs-1))} ; do
		startpt=$((i*sources_per_job))
		endpt=$((sources_per_job+startpt))
		dprint 2 "remove_short_sources_r $endpt $startpt > $dir/sources_job_$i &"
		remove_short_sources_r $endpt $startpt > $dir/sources_job_$i &
	done ; wait
	for i in {0..$((num_jobs-1))} ; do
		dshell 2 cat $dir/sources_job_$i
	done
	leftovers_start=$((num_jobs*sources_per_job))
	if [[ $leftovers_start -lt $num_sources ]] ; then
		leftovers=$((num_sources-leftovers_start))
		dprint 2 "leftovers_start: $leftovers_start, leftovers: $leftovers, num_sources: $num_sources"
		remove_short_sources_r $num_sources $leftovers_start
	fi
	
}

function remove_short_sources() {
	num_sources="$(wc -l ${dir}/sources | cut -d\  -f 1)"
	dprint 0 "Total sources: $num_sources"
	dprint 0 "Removing sources less than $minimum_clip_length seconds long..."
	ml=$((minimum_clip_length * 1000))
	ml=$(floor $ml)
	if [[ $parallelism -gt 0 ]]; then
		remove_short_sources_parallel $num_sources
	else
		remove_short_sources_r $num_sources 0 
	fi > $dir/sources2
	mv $dir/sources{2,}
	dprint 0 ""
	dprint 0 "Current sources: $(wc -l $dir/sources)"
}

function initial_setup() {

	export total_length=$(getLength $audiofile)
	export total_frames=$(( ($total_length*1.0) * $fps ))
	export total_clips=$(( ($total_length*1.0) / $cps ))
	export clip_length=$(( 1.0/cps )) 
	if [[ $((minimum_clip_length*1000)) -lt $(floor $((clip_length*1000))) ]] ; then
		export minimum_clip_length=$clip_length
	fi
	export clip_frames=$(floor $(( 0.5 + ( (1.0*fps) / cps ) )) )


	mkdir -p $dir/clip
	for i in "$@" ; do
		find "$@" -type f
	done > $dir/sources
	remove_short_sources
	print_summary
}

function teardown() {
	rm -rf $dir
}

function wrap() {
	cmd=$1 ; shift
	$cmd "$@" 1>&2
}

function quiet_wrap() {
	dl=$1
	shift
	if [[ "$dl" -le "$DEBUGLEVEL" ]] ; then
		wrap "$@"
	else
		wrap "$@" 2>/dev/null
	fi
}

function mplayer_wrap() {
	quiet_wrap 2 mplayer "$@"
}

function mencoder_wrap() {
	quiet_wrap 2 mencoder "$@"
}

function areWeUsingFrames() {
	[[ ${#enabled_filters} -gt 0 ]]
}

function checkFramesOK() {
	[[ $(find $1 -type f | wc -l) -ge $clip_frames ]]
}
function normalizeFrames() {
	find $1 -type f | head -n $clip_frames > $dir/cliplist
}

function clip2Frames() {
	pushd $4
	st=$1 ; end=$2 ; source=$3
	if [[ ${enabled_filters[(ie)mat]} -le ${#enabled_filters} ]] ; then
		dprint 2 "mat filter enabled: disabling vf scale"
		mplayer_wrap -quiet -ao null -vo jpeg -ss $st -endpos $end "$source"
	else
		mplayer_wrap -quiet -ao null -vo jpeg -vf scale=$resolution -ss $st -endpos $end "$source"
	fi
	popd
}

function frames2Clip() {
	frames=$(wc -l < $dir/cliplist)
	current_frame=$((current_frame + frames))
	delta=$(floor $(( current_secs*fps - current_frame )) )
	if [ $delta -gt 0 ] ; then
		i=0
		thing="$(tail -n 1 $dir/cliplist)"
		while [[ $i -lt $delta ]] ; do
			echo "$thing" >> $dir/cliplist
			i=$((i+1))
		done
	fi
	mencoder_wrap -quiet -oac copy -ovc lavc -vf scale=$resolution -mf fps=$fps -o $dir/clip-${current_clips}.avi $(cat $dir/cliplist | sed 's/^/mf:\/\//' | head -n $clip_frames )
}

function frameCleanup() {
	rm -f $dir/cliplist
	rm -rf $1
	mkdir $1
}

function clipExtractSuccess() {
		export current_clips=$((current_clips + 1))
		export current_secs=$((current_secs + clip_length)) 
}

function extractClip() {
	clipdir=$dir/clip
	st=$1 ; cl=$2 ; source=$3
	end=$((1+cl))
	dprint 1 "Getting clip: $(echo $st | sed 's/\.$//')s:$(echo $((st+end)) | sed 's/\.$//')s of \"$source\"..."
	if [[ areWeUsingFrames ]] ; then
		clip2Frames $st $end $source $clipdir
		if checkFramesOK $clipdir ; then
			dprint 2 "Clipdir=$clipdir ; $(find $clipdir -type f | wc -l) frames"
			normalizeFrames $clipdir
			applyFilters	$clipdir
			frames2Clip
			frameCleanup $clipdir
			clipExtractSuccess
		else
			dprint 2 "Clipdir=$clipdir ; $(find $clipdir -type f | wc -l) frames"
			dprint 1 "Frames not OK"
			extractRandomClip
		fi
	else
		dprint 1 "No frames"
		mencoder_wrap -quiet -oac copy -ovc lavc -vf scale=$resolution -mf fps=$fps -o $dir/clip-${current_clips}.avi -ss $st -endpos $end "$source"
		clipExtractSuccess
	fi
}

function mergeClips() {
	dprint 1 "Merging clips"
	setopt SH_WORD_SPLIT
	export lastmerge=$current_clips
	export cliplist=$(
		i=$(floor $((current_clips-9)) )
		if [[ $i -lt 0 ]] ; then i=0 ; fi
		while [[ $i -lt $(floor $((current_clips + 1)) ) ]] ; do echo $dir/clip-$i.avi ; i=$((i+1)) ; done 
	)
	if [[ -e $dir/clip.avi ]] ; then
		mencoder_wrap -quiet -oac copy -ovc copy -vf scale=$resolution -o $dir/clip-new.avi $dir/clip.avi $cliplist
		mv $dir/clip-new.avi $dir/clip.avi
	else
		mencoder_wrap -quiet -oac copy -ovc copy -vf scale=$resolution -o $dir/clip.avi $cliplist
	fi
	for item in $cliplist ; do rm -f $item ; done
	unsetopt SH_WORD_SPLIT
}


function extractRandomClip() {
	source=$(shuf -n 1 < $dir/sources)
	if [[ areWeUsingFrames ]] ; then
		lenCmd=getLengthAdjusted
	else
		lenCmd=getLength
	fi
	sl=$(floor $($lenCmd "$source"))
	while [[ $(floor $((sl*1000))) -lt $(floor $((minimum_clip_length * 1000))) ]] ; do	
		source=$(shuf -n 1 < $dir/sources)
		sl=$(floor $($lenCmd "$source"))
	done
	cl=$clip_length
	if [[ areWeUsingFrames ]] ; then
		targetFPS=$(getFPS "$source")
		cl=$(convertLength $cl $targetFPS)
	fi	

	st=$(( RANDOM%(sl-cl) ))
	if [[ areWeUsingFrames ]] ; then
		st=$(convertLengthInverse $st $targetFPS)
	fi
	dprint 2 "st: $st cl: $cl length: $(getLength "$source") fps: $(getFPS "$source")"
	extractClip $st $cl $source

	check=$(floor $((current_clips % 10)) )
	if [[ $check -eq 0 ]] ; then
		mergeClips
	fi
}

function main() {

	process_args "$@"

	current_secs=0
	current_frame=0
	current_clips=0
	lastmerge=1
	dprint 1 "Total length: $total_length"
	while [[ `floor $current_secs` -le `ceil $total_length` ]] ; do
		echo "$current_secs seconds / $total_length seconds completed"
		extractRandomClip
	done
	mergeClips
	dprint 1 "Creating final video"
	mencoder_wrap -quiet -oac pcm -ovc lavc -audiofile "$audiofile" -vf scale=$resolution -o "$outfile" $dir/clip.avi
	teardown
}

main "$@"
