x := Object clone do(
	children := List clone
	r := method(
		self children foreach(c, c print)
		self children foreach(c, c ?r)
		self children foreacn(c, c print)
	)
)

y := x clone
x children append(y)
"start" println
x r 
"end" println

