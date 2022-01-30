def fun(n):
    if(n==1):
        print("hello")
    elif(n==2):
        print("hii")
    elif(n==3):
        print("whatapp")
n=int(input("enter a number in the from 1,2 and 3:"))
if(n<1 or n>3):
    print("ERROR!!!\nenter a number from 1,2 and 3")
else:
    fun(n)
