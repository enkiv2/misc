(while : ; do 
	post "$(shuf -n 1 ~/.linkit | sed 's/^\([^\t]*\)\t\([^\t]*\).*$/Random link from the archives: \1 originally posted \2/')" 
	sleep 4h
done 2>&1) > /dev/null 

