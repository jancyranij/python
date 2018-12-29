def crange(n):
	if x in range(1,11):
		print('yes')
	else :
		print('no')
def main():
	try:
		x=int(input())
		crange(x)
	except:
		print('invalid')
		
main()
