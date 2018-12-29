def countd(x):
	print(x+1)
def main():
	try:
		x=int(input())
		countd(x)
	except:
		print('invalid')
main()
