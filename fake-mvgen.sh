#!/usr/bin/env zsh

available_filters=(randomColorScene randomColorFrame zoomIn zoomOut randomZoom)
enabled_filters=(randomColorScene randomZoom)
minimum_clip_length=0
parallelism=0
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
function help() {
	dprint 0  "Usage: $cmdname audiofile fps cps outfile [options...] source_directory [source_directory...]"
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
	dprint 0 "    -m length\tSpecify minimum clip length in seconds (default 1/cps)"
	dprint 0 "    -p threads\tSpecify parallelism (default: $parallelism)"
	exit 1
}


function getLength() {
	(mplayer -vo null -ao null -identify -frames 0 "$@" | (grep '^ID_LENGTH=[0-9\.]*$' || echo 0) | sed 's/^ID_LENGTH*=//' )2>/dev/null
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
			echo "$x"
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

function convertHelper() {
	item="$1" ; shift
	rm -f ${item}-2.jpeg
	dprint 0 "Running shell command: " convert "$item" "$@" "${item}-2.jpeg"
	convert "$item" "$@" "${item}-2.jpeg"
	dprint 0 "convert finished"
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
function filter_zoomIn() {
	dprint 2 "Zooming in on scene"
	count=$(wc -l < $dir/cliplist)
	delta=$((200/count))	# hard-code to zoom to middle 240x80 pixel square, on 640x480 image
	i=0
	for item in $(cat $dir/cliplist) ; do
		( 
			convertHelper $item -crop $(( 640-(2*i*delta) ))x$(( 480-(2*i*delta) ))+$((i*delta))+$((i*delta)) +repage 
		) &
		i=$((i+1))
		if [[ $i -gt $parallelism ]] ; then
			dprint 2 "Waiting for zoom to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done; wait
}
function filter_zoomOut() {
	dprint 2 "Zooming out on scene"
	count=$(wc -l < $dir/cliplist)
	delta=$((200/count))	# hard-code to zoom to middle 240x80 pixel square, on 640x480 image
	i=0
	for item in $(tac $dir/cliplist) ; do
		(
			convertHelper $item -crop $(( 640-(2*i*delta) ))x$(( 480-(2*i*delta) ))+$((i*delta))+$((i*delta)) +repage
		) &
		i=$((i+1))
		if [[ $i -gt $parallelism ]] ; then
			dprint 2 "Waiting for zoom to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done; wait
}
function filter_randomZoom() {
	if [[ $((RANDOM%2)) -gt 0 ]] ; then
		filter_zoomIn
	else
		filter_zoomOut
	fi
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
	[[ $# -lt 5 ]] && help
	[[ "$1" == "-h" ]] && help

	export audiofile=$1
	export fps=$2
	export cps=$3
	export outfile=$4
	shift ; shift ; shift ; shift
	
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
	drpint 0 "= Number of threads: $parallelism"
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

function remove_short_sources() {
	num_sources="$(wc -l ${dir}/sources | cut -d\  -f 1)"
	dprint 0 "Total sources: $num_sources"
	dprint 0 "Removing sources less than $minimum_clip_length seconds long..."
	ml=$((minimum_clip_length * 1000))
	ml=$(floor $ml)
	i=0
	while [[ $i -lt num_sources ]] ; do
		x="$(get_file_line $i $dir/sources)"
		print_if_long_enough "$x"
		i=$((i+1))
	done > $dir/sources2
	mv $dir/sources{2,}
	dprint 0 ""
	dprint 0 "Current sources: $(wc -l $dir/sources)"
}

function initial_setup() {

	export total_length=$(getLength $audiofile)
	export total_frames=$(( ($total_length*1.0) * $fps ))
	export total_clips=$(( ($total_length*1.0) / $cps ))
	export clip_length=$(( 1.0/cps )) 
	if [[ $minimum_clip_length -lt $(floor $clip_length) ]] ; then
		export minimum_clip_length=$clip_length
	fi
	export clip_frames=$(floor $(( 0.5 + ( (1.0*fps) / cps ) )) )

	export resolution="640:480"

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
	[[ $(ls $1 | wc -l) -gt 0 ]]
}
function normalizeFrames() {
	frame_count=$(ls $1 | wc -l)
	frame_ratio=$(floor $(( (1.0*frame_count) / clip_frames )) )
	frame_ratio_i=$(floor $(( (1.0*clip_frames) / frame_count )) )
	ls $1/* | (
		if [[ $frame_ratio -gt 1 ]] ; then
			skip $frame_ratio
		elif [[ $frame_ratio_i -gt 1 ]] ; then
			dup $frame_ratio_i
		else
			cat
		fi
	) > $dir/cliplist
}

function clip2Frames() {
	pushd $4
	st=$1 ; end=$2 ; source=$3
	mplayer_wrap -quiet -ao null -vo jpeg -vf scale=$resolution -ss $st -endpos $end "$source"
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
	rm -f $1/*
}

function clipExtractSuccess() {
		export current_clips=$((current_clips + 1))
		export current_secs=$((current_secs + clip_length)) 
}

function extractClip() {
	clipdir=$dir/clip
	st=$1 ; source=$2
	end=$((1+clip_length))
	dprint 1 "Getting clip: $(echo $st | sed 's/\.$//')s:$(echo $((st+end)) | sed 's/\.$//')s of \"$source\"..."
	if [[ areWeUsingFrames ]] ; then
		clip2Frames $st $end $source $clipdir
		if checkFramesOK $clipdir ; then
			dprint 1 "Clipdir=$clipdir ; $(ls $clipdir/* | wc -l) frames"
			normalizeFrames $clipdir
			applyFilters	$clipdir
			frames2Clip
			frameCleanup $clipdir
			clipExtractSuccess
		else
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
	sl=$(floor $(getLength "$source"))
	while [[ $(floor $((sl*1000))) -lt $(floor $((minimum_clip_length * 1000))) ]] ; do	
		source=$(shuf -n 1 < $dir/sources)
		sl=$(floor $(getLength "$source"))
	done

	st=$(( RANDOM%(sl-clip_length) ))
	extractClip $st $source

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
