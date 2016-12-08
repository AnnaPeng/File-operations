f = open("20161109 copy.csv", "r")
re = open("20161109 ready1.csv","w")

for line in f:
	line = str(line)
	line = line.split(",")
	for i, word in enumerate(line):
		if i!=5:
			re.write('"'+word+'"'+",")
		else:
			re.write('"'+word.strip()+'"'+"\n")
f.close()
re.close()