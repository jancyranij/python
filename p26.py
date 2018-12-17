n=input("enter the number:");
while(n!=0):
     re=re*10;
     re=re+n%10;
     n=n/10;
print("reverse of the number",re);
return 0
