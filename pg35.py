n=input("enter the string")
count=0
for x in n:
    if(x.isdigit()):
        count=count+1
print(count)
