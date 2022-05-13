#!/usr/bin/env zsh

cmdname=$0
pid=$$
function help() {
	echo "Usage: $cmdname audiofile fps cps outfile source_directory [source_directory...]"
	exit 1
}



function getLength() {
	(mplayer -vo null -ao null -identify -frames 0 "$@" | grep LENGTH | sed 's/^.*=//' )2>/dev/null
}
function floor() {
	echo "$@" | cut -d. -f 1
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
	echo "Coloring scene: $color"
	i=0
	for item in $(cat ~/.$$-cliplist) ; do
		( convert $item -fill "$color" -tint 110 ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
			echo "Waiting for color correction to finish on batch...\c"
			wait
			echo "\tdone"
			i=0
		fi
	done; wait
}
function filter_randomColorFrame() {
	# random color scene
	i=0
	for item in $(cat ~/.$$-cliplist) ; do
		( rm -f ${item}-2.jpeg ; convert $item -fill "$(randomColor)" -tint 110 ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
			echo "Waiting for color correction to finish on batch...\c"
			wait
			echo "\tdone"
			i=0
		fi
	done; wait
}
function filter_zoomIn() {
	echo "Zooming in on scene"
	count=$(wc -l < ~/.$$-cliplist)
	delta=$((200/count))	# hard-code to zoom to middle 240x80 pixel square, on 640x480 image
	i=0
	for item in $(cat ~/.$$-cliplist) ; do
		( rm -f ${item}-2.jpeg ; convert $item -crop $(( 640-(2*i*delta) ))x$(( 480-(2*i*delta) ))+$((i*delta))+$((i*delta)) +repage ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
			echo "Waiting for zoom to finish on batch...\c"
			wait
			echo "\tdone"
			i=0
		fi
	done; wait
}
function filter_zoomOut() {
	echo "Zooming out on scene"
	count=$(wc -l < ~/.$$-cliplist)
	delta=$((200/count))	# hard-code to zoom to middle 240x80 pixel square, on 640x480 image
	i=0
	for item in $(tac ~/.$$-cliplist) ; do
		( rm -f ${item}-2.jpeg ; convert $item -crop $(( 640-(2*i*delta) ))x$(( 480-(2*i*delta) ))+$((i*delta))+$((i*delta)) +repage ${item}-2.jpeg &&
		mv ${item}{-2.jpeg,} ) &
		i=$((i+1))
		if [[ $i -gt 20 ]] ; then
			echo "Waiting for zoom to finish on batch...\c"
			wait
			echo "\tdone"
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

function process_args() {
	[[ $# -lt 5 ]] && help
	[[ "$1" == "-h" ]] && help

	export audiofile=$1
	export fps=$2
	export cps=$3
	export outfile=$4
	shift ; shift ; shift ; shift

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

function main() {

	process_args "$@"

	current_secs=0
	current_frame=0
	current_clips=0
	lastmerge=1
	echo "Total length: $total_length"
	while [[ `floor $current_secs` -lt `floor $total_length` ]] ; do
		echo "$current_secs seconds / $total_length seconds completed"
		source=$(shuf -n 1 < ~/.$$-sources)
		sl=$(floor $(getLength "$source"))
		sl2=$(floor $((sl*1000)) )
		cl=$(floor $((clip_length*1000)) )
		if [[ $sl2 -gt $cl ]] ; then
			st=$(( RANDOM%(sl-clip_length) ))
			end=$((1+clip_length))
			pushd ~/.$$-clip
			mplayer -quiet -ao null -vo jpeg -vf scale=$resolution -ss $st -endpos $end "$source"
			frame_count=$(ls | wc -l)
			if [[ $frame_count -eq 0 ]] ; then continue ; fi
			frame_ratio=$(floor $(( (1.0*frame_count) / clip_frames )) )
			frame_ratio_i=$(floor $(( (1.0*clip_frames) / frame_count )) )
			if [[ $frame_ratio -gt 1 ]] ; then
				ls | skip $frame_ratio > ~/.$$-cliplist
			elif [[ $frame_ratio_i -gt 1 ]] ; then
				ls | dup $frame_ratio_i > ~/.$$-cliplist
			else
				ls > ~/.$$-cliplist
			fi
			
			# filters go here
			filter_randomColorScene
			filter_randomZoom

			frames=$(wc -l < ~/.$$-cliplist)
			current_frame=$((current_frame + frames))
			current_clips=$((current_clips + 1))
			current_secs=$((current_secs + clip_length)) 
			delta=$(floor $(( current_secs*fps - current_frame )) )
			if [ $delta -gt 0 ] ; then
				i=0
				thing="$(tail -n 1 ~/.$$-cliplist)"
				while [[ $i -lt $delta ]] ; do
					echo "$thing" >> ~/.$$-cliplist
					i=$((i+1))
				done
				rm -f ~/.$$-temp
			fi
			mencoder -quiet -oac copy -ovc lavc -vf scale=$resolution -mf fps=$fps -o ~/.$$-clip-${current_clips}.avi $(cat ~/.$$-cliplist | sed 's/^/mf:\/\//' | head -n $clip_frames )
			popd
			rm -f ~/.$$-cliplist
			rm -f ~/.$$-clip/*
			check=$(floor $((current_clips % 10)) )
			if [[ $check -eq 0 ]] ; then
				setopt SH_WORD_SPLIT
				lastmerge=$current_clips
				cliplist=$(i=$(floor $((current_clips-9)) ) ; while [[ $i -lt $(floor $((current_clips + 1)) ) ]] ; do echo ~/.$$-clip-$i.avi ; i=$((i+1)) ; done )
				if [[ -e ~/.$$-clip.avi ]] ; then
					mencoder -quiet -oac copy -ovc copy -vf scale=$resolution -o ~/.$$-clip-new.avi ~/.$$-clip.avi $cliplist
					mv ~/.$$-clip-new.avi ~/.$$-clip.avi
				else
					mencoder -quiet -oac copy -ovc copy -vf scale=$resolution -o ~/.$$-clip.avi $cliplist
				fi
				for item in $cliplist ; do rm $item ; done
				unsetopt SH_WORD_SPLIT
			fi
		else
			echo "Clip too small: $clip_length > $sl on file \"$source\"; skipping"
		fi
	done
	setopt SH_WORD_SPLIT
	cliplist=$(i=$lastmerge ; while [[ $i < $((current_clips + 1)) ]] ; do echo ~/.$$-clip-$i.avi ; i=$((i+1)) ; done )
	if [[ -e ~/.$$-clip.avi ]] ; then
		mencoder -quiet -oac copy -ovc copy -vf scale=$resolution -o ~/.$$-clip-new.avi ~/.$$-clip.avi $cliplist
		mv ~/.$$-clip-new.avi ~/.$$-clip.avi
	else
		mencoder -quiet -oac copy -ovc copy -vf scale=$resolution -o ~/.$$-clip.avi $cliplist
	fi
	for item in $cliplist ; do rm $item ; done
	unsetopt SH_WORD_SPLIT
	mencoder -quiet -oac pcm -ovc lavc -audiofile "$audiofile" -vf scale=$resolution -o "$outfile" ~/.$$-clip.avi
	rm ~/.$$-clip.avi
	rmdir ~/.$$-clip
	rm ~/.$$-sources
}

main "$@"
