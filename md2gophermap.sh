sed 's/\[\([^]]*\)](\([^)]*\))/\nh\t\t\1\tURL:\2\n/g' | sed 's/^/i/' | sed 's/^ih\t\t/h/' | fmt -s -pi
