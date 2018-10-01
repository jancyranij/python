print("print maximum element")
from array import*
n=int(input("N="))
for y in range(1,n+1):
   z=array('i',[y])
m=z[0]
for x in z:
   if(x<=z[0]):
       m=x
print("maxi",m)
