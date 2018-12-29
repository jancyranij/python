try:
        x=int(input())
        str=''
        while(x!=0):
                stri+=str(x%10)
                x//=10
        for z in range(len(str)-1,-1,-1):
                print(stri[z])
except:
        print('invalid')
