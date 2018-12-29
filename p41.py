def printv(valu,m):
	for a in range(m):
		print(valu)

def main():
	try :
		value=input()
		m=int(input())
		printv(value,m)
	except:
		print('invalid ')
main()
