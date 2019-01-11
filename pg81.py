import sys
 def getl():
	x=[]
	y=[]
	while(True):
		try:
			a,b = map(int,sys.stdin.readline().split())
		except ValueError:
			break
		x.append(a)
		x.append(b)
		y.append(x)
		x=[]
	for i in y:
		print(i[1]-i[0])
try:
	getx()
except:
	print('invalid')
