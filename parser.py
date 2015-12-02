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
	g.write("out.println(")
	g.write(quote)
	if("\"" in line):
		elems=line.split('"')
		for i in elems:
			g.write(i)
			g.write(slash)
			g.write(quote)
	else:
		g.write(line)
	g.write(quote)
	g.write(");\n")
f.close()
g.close()
