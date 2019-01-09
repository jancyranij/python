try:
	z=int(input())
	for x in range(z):
		q=2**x
		if q>z:
			print(q)
			break
except:
	print('invalid')
