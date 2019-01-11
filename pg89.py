def lex():
	t=input()
	l=list(t)
	l.sort()
	g=''.join(l)
	print(g)
try:
	lex()
except:
	print('invalid')
