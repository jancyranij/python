def oddeven(x):
        if x%2==0:
                print("even")
        else:
                print("odd")
def m2():
        try:
                y=int(input())
                x=int(input())
                oddeven(y*x)
        except:
                print('invalid')
