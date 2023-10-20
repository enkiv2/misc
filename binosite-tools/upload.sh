#!/usr/bin/env zsh

failed=""

function upload() {
	scp -r "$@" accela_miniaturebinoculars@ssh.nyc1.nearlyfreespeech.net:/home/public/ 
}


for i in "$@" ; do
	upload $i || (
		echo "Upload failed for $i ; retrying (try 2)..."
		upload $i || (
			echo "Upload failed for $i ; retrying in 5s (try 3)..."
			sleep 5
			upload $i || (
				echo "Upload failed for $i ; retrying in 1m (try 4)..."
				sleep 1m
				upload $i || (
					echo "Upload failed for $i after 4 tries."
					failed="$failed $i"
				)
			)
		)
	)
done

[ -z $failed ] || ( echo "Failed: $failed" ; exit 1 )
