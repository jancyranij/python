def between():
	u=int(input())
	w=int(input())
	v=int(input())
	for i in range(w,v):
		if i==u:
			return 'yes'
	return 'no'
try:
	between()
except:
	print('invalid')
