def main():
	try:
		a=int(input())
		b=int(input())
		l=a
		a=b
		b=l
		print(a,b)
	except:
		print('invalid')
main()
