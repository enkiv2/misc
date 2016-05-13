#!/usr/bin/env zsh
youtube-dl -o "%(playlist_title)s-%(playlist_index)s-%(uploader)s-%(title)s.%(ext)s" --write-sub --write-auto-sub -i "$@"

