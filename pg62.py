def checkbin():
	m=['0','1']
	n=0
	s=input()
	for x in range(len(s)):
		if st[x] in m:
			continue
		else :
			n=1
			break
	if n!=1:
		print('yes')
	else :
		print('no')
