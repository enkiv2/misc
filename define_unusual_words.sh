#!/usr/bin/env zsh
strings | tr 'A-Z_:' 'a-z  ' | tr ' ' '\n' | tr -d ',.`?";~' | grep '[a-z]' | sed "s/'$//" | awk '/^.*-$/{ax=$0; processed=1;} { if (processed) { processed = 0 } else { if (ax) { print ax $0 ; ax="" ; } else { print $0 ;} } }' | tr -d '-' | awk '{if ((++ax[$0])==2) { print $0 } }' | while read x ; do grep -iq "^$x\$" /usr/share/dict/words || echo "$x" ; done | ./defines.sh
