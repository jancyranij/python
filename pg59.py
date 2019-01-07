def ml(l):
	m=0
	for x in l:
		if m<x:
			m=x
	print(m)
def main():
	try:
		l=[1,2,3,5,4,77,4,24,52,4]
		ml(l)
	except:
		print('invalid')
main()
