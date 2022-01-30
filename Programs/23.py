#functions
def fun(n):
    if(n==1):
        return "hello"
    elif(n==2):
        return "hii"
    elif(n==3):
        return "whatapp"
n=int(input("enter a number from 1,2 and 3:"))
if(n<0 or n>3):
    print("ERROR!!\nenter a number from 1,2 and 3 only....")
else:
    print(fun(n))
