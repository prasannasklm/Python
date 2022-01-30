#count no.of digits in an integer
n=int(input("enter a number:"))
t=n
c=0
while(n>0):
    c=c+1
    n=n//10
print("no.of digits in the entered integer is:",c)
