#check whether entered number is prime or not
n=int(input("enter a number:"))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if(c==2):
    print("enterd number is prime number!!!")
else:
    print("not a Prime number")
