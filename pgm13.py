print("CHECK WHETHER A NUMBER IS PRIME OR NOT")
N=int(input("enter the number"))
s=0
for x in range (1,N+1) :
    if(N%x==0):
        s=s+1
if(s==2):
 print("prime")
else:
    print("not")
