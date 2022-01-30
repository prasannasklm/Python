#largest number among 3 numbers
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if(a>b and a>c):
    print(a,"is largest number...")
elif(b>a and c>a):
    print(b,"is largest number...")
elif(c>a and c>b):
    print(c,"is largest number...")
