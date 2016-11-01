def lovecraftParas():
	buf=""
	while(len(buf.split())<50000):
		buf+=lovecraftPara()+"\n\n"
	return buf

