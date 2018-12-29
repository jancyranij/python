def cmp(str1,str2):
	for x in range(len(str2)):
		str1+=str2[x]
	print(str1)
def main():
	try:
		s1=input()
		s2=input()
		cmp(s1,s2)
	except:
		print('invalid')
main()
