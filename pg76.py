def compo():
	n=int(input())
	g=0
	for i in range(2,n//2):
		if n%i==0:
			g=1
			break
	if g==1:
		print('yes')
	else :
		print('no')
try:
	compo()
else :
	print('invalid')
