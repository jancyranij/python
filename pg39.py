x=[]
    n=10
    for z in range(0,n):
        y=int(input("enter elements:"))
        x.append(y)
    x.sort()
    print("largest element",x[n-1])
