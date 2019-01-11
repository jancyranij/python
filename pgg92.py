def sumall():
	f=int(input())
	l=[]
	sum=0
	for x in range(f):
		l.append(int(input()))
		sum+=l[x]
	print(sum);
try:
	sumall()
except:
	print('invalid');
