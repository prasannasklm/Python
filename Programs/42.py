#armstrong number
n=int(input("enter a number:"))
s=0
t=n
while(t>0):
    r=t%10
    s=s+r*r*r
    t=t//10
if(s==n):
    print("armstrong number")
else:
    print("not an armstrong number")
