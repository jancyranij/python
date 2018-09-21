print("check whether a number is palindrome or not")
n=int(input("n="))
if(n<=1000):
    x=n
    rev=0
    while n>0:
     re=n%10
     rev=rev*10+re
     n=n//10
    if(x==rev):
      print("yes")
    else:
       print("not")
