def countd(x):
	n=0
	while(x!=0):
		x//=10
		c+=1
	print(n)
def main():
	try:
		x=int(input())
		countd(x)
	except:
		print('invalid')
main()
