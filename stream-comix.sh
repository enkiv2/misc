#!/usr/bin/env zsh

cmd=$0
delay=$1 ; shift

extdir=~/.stream-comix/$$/

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
		;;
		mp4)
			pushd "$extdir"
			mplayer -ao null -vo jpeg	"$@"
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

		
