def composites():
	a=int(input())
	l=[]
	f=0
	for x in range(1,a//2+1):
		if a%x==0:
			l.append(x)
	l.append(a)
	for x in l:
		print(x)
try:
	composites()
except:
	print('invalid')
