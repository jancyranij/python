def isogramm():
	a=input()
	l=list(a)
	t=[]
	for x in l:
		if not x in t:
			t.append(i)
	if len(l)==len(t):
		print('yes')
	else :
		print('no')
try:
	isogramm()
except:
	print('invalid')
