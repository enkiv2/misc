#!/usr/bin/env zsh

cmd=$0
delay=$1 ; shift

basedir=~/.stream-comix/
extdir=${basedir}/$$/
mkdir -p $extdir

( # Cleanup mechanism: upon startup, remove temp dirs not corresponding to currently running PIDs
	cd $basedir && (
		ps aux | awk '{print $2}' > $extdir/.live-pids
		echo * | tr ' ' '\n' | while read x ; do
			grep -q "^$x\$" $extdir/.live-pids || (rm -rf $x || (umount $x && rm -rf $x) || echo "Could not clean up tempdir $basedir/$x" > /dev/stderr )
		done
		rm -f $extdir/.live-pids
	)
)

function recurse_stream() {
	mkdir -p $extdir
	type=$1 ; shift

	echo -e "=====\n\ttype: $type\n\tfilename: $@\n\textdir: $extdir\n=====\n"

	case $type in
		zip)
			unzip "$@" -d "$extdir"
		;;
		rar)
			unrar -x "$@" "$extdir"
		;;
		pdf)
			convert "$@" "$extdir/%3d.jpg"
		;;
		html)
			pandoc "$@" "$extdir/out.pdf"
		;;
		iso)
			fuseiso "$@" "$extdir"
			$cmd $delay $extdir
			umount "$extdir"
			return
		;;
		mp4)
			path="$(realpath "$@")"
			pushd "$extdir"
			mplayer -ao null -vo jpeg	"$path"
			popd
		;;
		*)
			feh --bg-max "$@" &&
			feh --bg-tile ~/Downloads/dingir.jpg &&
			feh --bg-max "$@" && sleep $delay
			return
		;;
	esac
	$cmd $delay $extdir
	rm -rf $extdir
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
	echo "Showing $dir"
	find $dir -type f
done) | sort | while read x ; do 
	echo "file: $x"
	type=$(echo "$x" | sed "$rules" | tr 'A-Z' 'a-z' | sed 's/^.*\.\([^.]*\)$/\1/')
	recurse_stream "$type" "$x"
done

		
