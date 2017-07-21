#!/usr/bin/env zsh
torify w3m -dump "https://en.m.wikipedia.org/wiki/Special:RandomInCategory/Featured_articles" | tail -n +11
