#!/usr/bin/env zsh

DEBUGLEVEL=0

cmd=$0
delay=$1 ; shift

basedir=~/.stream-comix/
extdir=${basedir}/$$/
mkdir -p $extdir

function dprint() {
	level=$1 ; shift
	if [[ "$level" -lt "$DEBUGLEVEL" ]] ; then
		echo -e "$@"
	fi
}

function quiet() {
	level=$1 ; shift
	while read -r x ; do
		dprint "$level" "$x"
	done
}

( # Cleanup mechanism: upon startup, remove temp dirs not corresponding to currently running PIDs
	cd $basedir && (
		ps aux | awk '{print $2}' > $extdir/.live-pids
		echo * | tr ' ' '\n' | while read x ; do
			grep -q "^$x\$" $extdir/.live-pids || (rm -rf $x || (umount $x && rm -rf $x) || echo "Could not clean up tempdir $basedir/$x" > /dev/stderr ) |& quiet 1
		done
		rm -f $extdir/.live-pids
	)
)

function extract_by_type() {
	type=$1 ; shift
	case $type in
		zip)
			unzip "$@" -d "$extdir" |& quiet 2
		;;
		rar)
			unrar -x "$@" "$extdir" |& quiet 2
		;;
		pdf)
			convert "$@" "$extdir/%3d.jpg" |& quiet 2
		;;
		html)
			pandoc "$@" -o "$extdir/out.pdf" |& quiet 2
		;;
		iso)
			fuseiso "$@" "$extdir" |& quiet 2
		;;
		mp4)
			path="$(realpath "$@")"
			pushd "$extdir"
			mplayer -ao null -vo jpeg	"$path" |& quiet 2
			popd
		;;
	esac
}

function display_by_type() {
	type=$1 ; shift
	case $type in
		zip|rar|pdf|html|iso|mp4)
			$cmd $delay $extdir
		;;
		*)
			feh --bg-max "$@" &&
			feh --bg-tile ~/Downloads/dingir.jpg &&
			feh --bg-max "$@" && sleep $delay 				|& quiet 2
		;;
	esac	
}

function cleanup_by_type() {
	type=$1
	case $type in
		iso)
			umount $extdir
			rm -rf $extdir
		;;
		*)
			rm -rf $extdir
		;;
	esac
}

function recurse_stream() {
	mkdir -p $extdir
	type=$1 ; shift

	dprint 1 "=====\n\ttype: $type\n\tfilename: $@\n\textdir: $extdir\n=====\n"

	extract_by_type "$type" "$x"
	display_by_type "$type" "$x"
	cleanup_by_type "$type"
}

rules='
				s/\.cbz$/.zip/;
				s/\.cbr$/.rar/;
				s/\.xhtml$/.html/;
				s/\.htm$/.html/;
				s/\.xhtm$/.html/;
				s/\.doc$/.html/;
				s/\.docx$/.html/;
				s/\.epub$/.html/;
				s/\.mobi$/.html/;
				s/\.txt$/.html/;
				s/\.md$/.html/;
				s/\.ppt$/.html/;
				s/\.pttx$/.html/;
				s/\.\(wmv|mpeg|avi|mkv|mov|mpg|webm\)$/.mp4/'

(for dir in "$@" ; do
	dprint 1 "Showing $dir"
	find $dir -type f
done) | sort | while read x ; do 
	dprint 1 "File: $x"
	type=$(echo "$x" | sed "$rules" | tr 'A-Z' 'a-z' | sed 's/^.*\.\([^.]*\)$/\1/')
	recurse_stream "$type" "$x"
done

		
