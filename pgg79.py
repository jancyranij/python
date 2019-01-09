import math
def psqr():
	x=int(input())
	y=int(input())
	y*=x
	s=math.sqrt(y)
	if s==int(s):
		print('yes')
	else :
		print('no')
try:
	psqr()
except:
	print('invalid')
