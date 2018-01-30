#!/usr/bin/env io

doFile("kamui.io")
x := KUIWidget clone
x offset set(10, 20)
y := KUIContainer clone
y setParent(x)
y offset set(10, 20)

"Initial bbox for" println
"X:" println
x bbox println
"Y:" println
y bbox println
"Recalculating..." println
x calculateBbox
"New bbox for" println
"X:" println
x bbox println
"Y:" println
y bbox println


while(Scheduler yieldingCoros size > 1, yield)
