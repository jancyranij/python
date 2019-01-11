import sys
def gcdd():
	(a,b)=map(int,sys.stdin.readline().split())
	while(b!=0):
		t=b
		b=a%b
		a=t
	print(x)
try:
	gcdd()
except:
	print('invalid')
