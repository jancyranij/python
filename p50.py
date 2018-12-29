def main():
	try:
		z=0
		x=int(input())
		while(x!=0):
			x=x/2
			if x==1:
				z=1
				break
		if z!=1:
			print('no');
		else :
			print('yes');
	except:
		print('invalid');
main()
