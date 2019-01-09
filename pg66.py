try:
	z=int(input())
	flag=0
	for x in range(2,int(z/2)+1):
		if z%x ==0:
			flag=1
			break
	if flag==0:
		print('prime')
	else :
		print('not prime')
except:
print('invalid')
