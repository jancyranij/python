print("DISPLAY EVEN NUMBERS BETWEEN 2 INTERVALS")
a=int(input("enter the number"))
b=int(input("enter the number"))
for x in range(a+1,b):
    if(x%2==0):
        print(x)
else:
    print("invalid")
