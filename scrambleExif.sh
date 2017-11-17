#!/usr/bin/env zsh

for i in "$@" ; do
	lat=$((RANDOM%(360)-180+(RANDOM%10000000.0)/100000000))
	long=$((RANDOM%(180)-90+(RANDOM%10000000.0)/100000000))
	date="$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))$((RANDOM%10))"

	exiftool -s "$i"
	exiftool -exif:all= "$i"
	exiftool -v2 -d "%s" -xmp:dateTimeOriginal=$date -GPSLongitude=$long -GPSLatitude=$lat "$i"
done
