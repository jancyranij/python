def fibo(t):
	if t==1 or t==0:
		return(t)
	else :
		return fibo(t-1)+fibo(t-2)
try:
	t=int(input())
	sum=0
	for x in range(0,t):
		print(fibo(x))
except:
print('invalid')
