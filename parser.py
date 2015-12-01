import sys

try:
	fname=sys.argv[1]
except:
	print "Error : CL argument missing"
	exit()
f=open(fname,'r')
g=open('output','w')
slash="\\"
quote="\""
g.write("PrintWriter out = response.getWriter();\n")
for line in f:
	line=line.rstrip()
	elems=line.split('"')
	j=len(elems)
	k=0
	g.write("out.println(")
	g.write(quote)
	for i in elems:
		k+=1
		g.write(i)
		if(k<j-1):
			g.write(slash)
			g.write(quote)
	g.write(quote)
	g.write(");\n")
f.close()
g.close()
