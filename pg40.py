def f(a):
	if a==1 or a==0:
		return(a)
	else :
		return f(a-1)+f(a-2)
try:
	a=int(input('Enter a :'))
	sum=0
	for b in range(0,a):
		print(f(b))
except:
print('invalid')
