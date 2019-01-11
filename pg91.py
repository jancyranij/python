def suma():
	h=int(input())
	l=[]
	sum=0
	for j in range(h):
		l.append(int(input()))
		sum+=l[j]
	print(sum);
try:
	suma()
except:
	print('invalid');
