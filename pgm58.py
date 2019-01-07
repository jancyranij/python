def main():
	try:
		p=int(input())
		q=int(input())
		p=p^q
		q=p^q
		p=p^q
		print(p,q)
	except:
		print('invalid')
main()
