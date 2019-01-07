def firstk():
	string=input()
	g=''
	k=int(input())
	for i in range(0,k):
		g+=string[i]
	print(g)
try:
	firstk()
except:
	print('invalid')
