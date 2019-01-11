def s():
	(k,h,f)=map(int,sys.stdin.readline().split())
	sii=k*h*f/100
	print(math.floor(sii));
try:
	s()
except:
	print('invalid');
