#!/usr/bin/env zsh

available_filters=(randomColorScene randomColorFrame zoomIn zoomOut randomZoom)
enabled_filters=(randomColorScene randomZoom)
cmdname=$0
pid=$$

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
	dprint 0 "  -v\tVerbosity level 1"
	dprint 0 "  -vv\tVerbosity level 2"
	dprint 0 "  -vvv\tVerbosity level 3"
	exit 1
}


function getLength() {
	(mplayer -vo null -ao null -identify -frames 0 "$@" | grep LENGTH | sed 's/^.*=//' )2>/dev/null
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

function filter_randomColorScene() {
	# random color scene
	color="$(randomColor)"
	dprint 2 "Coloring scene: $color"
	i=0
	for item in $(cat ~/.$$-cliplist) ; do
		( convert $item -fill "$color" -tint 110 ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
			dprint 2 "Waiting for color correction to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done; wait
}
function filter_randomColorFrame() {
	# random color scene
	i=0
	for item in $(cat ~/.$$-cliplist) ; do
		(
			rm -f ${item}-2.jpeg
			convert $item -fill "$(randomColor)" -tint 110 ${item}-2.jpeg &&
				mv ${item}{-2.jpeg,} 
		) &
		i=$((i+1)
		)
		if [[ $i -gt 20 ]] ; then
			dprint 2 "Waiting for color correction to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done; wait
}
function filter_zoomIn() {
	dprint 2 "Zooming in on scene"
	count=$(wc -l < ~/.$$-cliplist)
	delta=$((200/count))	# hard-code to zoom to middle 240x80 pixel square, on 640x480 image
	i=0
	for item in $(cat ~/.$$-cliplist) ; do
		( rm -f ${item}-2.jpeg ; convert $item -crop $(( 640-(2*i*delta) ))x$(( 480-(2*i*delta) ))+$((i*delta))+$((i*delta)) +repage ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
			dprint 2 "Waiting for zoom to finish on batch...\c"
			wait
			dprint 2 "\tdone"
			i=0
		fi
	done; wait
}
function filter_zoomOut() {
	dprint 2 "Zooming out on scene"
	count=$(wc -l < ~/.$$-cliplist)
	delta=$((200/count))	# hard-code to zoom to middle 240x80 pixel square, on 640x480 image
	i=0
	for item in $(tac ~/.$$-cliplist) ; do
		( rm -f ${item}-2.jpeg ; convert $item -crop $(( 640-(2*i*delta) ))x$(( 480-(2*i*delta) ))+$((i*delta))+$((i*delta)) +repage ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
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

function initial_setup() {

	export total_length=$(getLength $audiofile)
	export total_frames=$(( ($total_length*1.0) * $fps ))
	export total_clips=$(( ($total_length*1.0) / $cps ))
	export clip_length=$(( 1.0/cps ))
	export clip_frames=$(floor $(( 0.5 + ( (1.0*fps) / cps ) )) )

	export resolution="640:480"

	mkdir ~/.${pid}-clip
	for i in "$@" ; do
		find "$@"
	done > ~/.${pid}-sources
}

function teardown() {
	rm ~/.${pid}-clip.avi
	rmdir ~/.${pid}-clip
	rm ~/.${pid}-sources
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
	) > ~/.${pid}-cliplist
}

function clip2Frames() {
	pushd $4
	st=$1 ; end=$2 ; source=$3
	mplayer_wrap -quiet -ao null -vo jpeg -vf scale=$resolution -ss $st -endpos $end "$source"
	popd
}

function frames2Clip() {
	frames=$(wc -l < ~/.${pid}-cliplist)
	current_frame=$((current_frame + frames))
	delta=$(floor $(( current_secs*fps - current_frame )) )
	if [ $delta -gt 0 ] ; then
		i=0
		thing="$(tail -n 1 ~/.${pid}-cliplist)"
		while [[ $i -lt $delta ]] ; do
			echo "$thing" >> ~/.${pid}-cliplist
			i=$((i+1))
		done
		rm -f ~/.$$-temp
	fi
	mencoder_wrap -quiet -oac copy -ovc lavc -vf scale=$resolution -mf fps=$fps -o ~/.${pid}-clip-${current_clips}.avi $(cat ~/.${pid}-cliplist | sed 's/^/mf:\/\//' | head -n $clip_frames )
}

function frameCleanup() {
	rm -f ~/.${pid}-cliplist
	rm -f $1/*
}

function clipExtractSuccess() {
		export current_clips=$((current_clips + 1))
		export current_secs=$((current_secs + clip_length)) 
}

function extractClip() {
	clipdir=~/.${pid}-clip
	st=$1 ; source=$2
	end=$((1+clip_length))
	dprint 1 "Getting clip: $(echo st | sed 's/\.$//')s:$(echo $((st+end)) | sed 's/\.$//')s of \"$source\"..."
	if [[ areWeUsingFrames ]] ; then
		clip2Frames $st $end $source $clipdir
		if checkFramesOK $clipdir ; then
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
		mencoder_wrap -quiet -oac copy -ovc lavc -vf scale=$resolution -mf fps=$fps -o ~/.${pid}-clip-${current_clips}.avi -ss $st -endpos $end "$source"
		clipExtractSuccess
	fi
}

function mergeClips() {
	dprint 1 "Merging clips"
	setopt SH_WORD_SPLIT
	export lastmerge=$current_clips
	export cliplist=$(i=$(floor $((current_clips-9)) ) ; while [[ $i -lt $(floor $((current_clips + 1)) ) ]] ; do echo ~/.$$-clip-$i.avi ; i=$((i+1)) ; done )
	if [[ -e ~/.$$-clip.avi ]] ; then
		mencoder_wrap -quiet -oac copy -ovc copy -vf scale=$resolution -o ~/.${pid}-clip-new.avi ~/.${pid}-clip.avi $cliplist
		mv ~/.${pid}-clip-new.avi ~/.${pid}-clip.avi
	else
		mencoder_wrap -quiet -oac copy -ovc copy -vf scale=$resolution -o ~/.$$-clip.avi $cliplist
	fi
	for item in $cliplist ; do rm -f $item ; done
	unsetopt SH_WORD_SPLIT
}


function extractRandomClip() {
	source=$(shuf -n 1 < ~/.$$-sources)
	sl=$(floor $(getLength "$source"))
	sl2=$(floor $((sl*1000)) )
	cl=$(floor $((clip_length*1000)) )
	if [[ $sl2 -gt $cl ]] ; then
		st=$(( RANDOM%(sl-clip_length) ))
		extractClip $st $source

		check=$(floor $((current_clips % 10)) )
		if [[ $check -eq 0 ]] ; then
			mergeClips
		fi
	else
		dprint 1 "Clip too small: $clip_length > $sl on file \"$source\"; skipping"
	fi
}

function main() {

	process_args "$@"

	current_secs=0
	current_frame=0
	current_clips=0
	lastmerge=1
	dprint 1 "Total length: $total_length"
	while [[ `floor $current_secs` -lt `ceil $total_length` ]] ; do
		echo "$current_secs seconds / $total_length seconds completed"
		extractRandomClip
	done
	mergeClips
	dprint 1 "Creating final video"
	mencoder_wrap -quiet -oac pcm -ovc lavc -audiofile "$audiofile" -vf scale=$resolution -o "$outfile" ~/.$$-clip.avi
	teardown
}

main "$@"
