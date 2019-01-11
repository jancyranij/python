num=int(input("Enter any number"))
b=0
for y in range(1,num+1):
	if(num%y==0):
		b=b+1
if(b>2):
	print("composite");
else:
        print("Not composite");
