def avg(l,x):
	s=0
	for n in range(x):
		s+=l[n]
	print(s/x);
def main():
	try:
		x=int(input())
		l=[]
		for n in range(x):
			l.append(int(input()))
		avg(l,x)
	except:
		print('invalid');
main()
