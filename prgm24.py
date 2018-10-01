n=int(input("enter the length:"))
list=[]
for i in range(0,n):
    newNumber=int(input("enter the numbers="))
    a=list.append(newNumber)
    print list
list.sort()
print("Sorted list",list)
