def kthno():
	l=[]
	(h,b)=map(int,sys.stdin.readline().split())
	for i in range(h):
		l.append(int(input()))
	print(l[b-1]);
try:
	kthno()
except:
	print('invalid');
