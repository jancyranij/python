def countd(l,n):
	(max,min)=(0,9999)
	for y in range(x):
		if max<l[y]:
			max=l[y]
		if min>l[y]:
			min=l[y]
	print(min,max);
def main():
	try:
		l=[]
		x=int(input())
		for y in range(x):
			l.append(int(input()))
		countd(l,x)
	except:
		print('invalid');
main()
