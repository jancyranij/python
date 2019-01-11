def string1to2():
	a=input()
	l=list(a)
	(d,o)=('','')
	for x in range(len(l)):
		if x%2==0:
			d+=l[x]
		else :
			o+=l[x]
	print(d,o)
try:
	string1to2()
except:
	print('invalid')
