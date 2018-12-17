n=input("enter the number:");
while(n!=0):
     r=r*10;
     r=r+n%10;
     n=n/10;
print("reverse",r);
return 0
