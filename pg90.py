def onlyint():
	h=input()
	l=list(h)
	g=''
	for b in l:
		if b.isnumeric():
			g+=b
	print(g)
try:
	onlyint()
except:
	print('invalid')

