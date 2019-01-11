def farmarea():
	x,m=map(float,sys.stdin.readline().split())
	n=x*m
	print(round(n,5))
try:
	farmarea()
except:
	print('invalid')
