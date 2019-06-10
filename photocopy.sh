#!/usr/bin/env zsh
# stolen from https://www.imagemagick.org/discourse-server/viewtopic.php?t=14441
convert $1 -colorspace gray -contrast-stretch 4%x0% \( +clone -blur 0x3 \) +swap -compose divide -composite -blur 0x1 -unsharp 0x20 $2
