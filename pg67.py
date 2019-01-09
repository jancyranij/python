def near10():
	z=int(input())
	while(True):
		if z%10==0:
			break
		z=z+1
	print(z)
try:
	near10()
except:
	print('invalid')
