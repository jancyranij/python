def od():
	x=int(input())
	e=[]
	while(x!=0):
		e.append(x%10)
		x//=10
	for j in range(len(e)-1,-1,-1):
		if e[j]%2!=0:
			print(e[j])
try:
	od()
except:
	print('invalid')
