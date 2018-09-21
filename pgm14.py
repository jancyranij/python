print("DISPLAY ODD NUMBERS BETWEEN 2 INTERVALS")
a=int(input("enter the number"))
b=int(input("enter the number"))
if(a<=100000)&(b<=10000):
    for x in range(a,b+1):
     if(x%2!=0):
        print(x)

else:
      print("invalid")
