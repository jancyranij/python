print("DISPLAY PRIME NUMBERS BETWEEN 2 INTERVALS")
a=int(input("enter the number"))
b=int(input("enter the number"))
s=0
for x in range(a+1,b):
    s=0
    for y in range(1,x+1):
        if(x%y==0):
            s=s+1
    if(s==2):
         print(x)
