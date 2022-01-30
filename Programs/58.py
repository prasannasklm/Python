#armstrong numbers in the interval
a=int(input("enter lower bound:"))
b=int(input("enter upper bound:"))
for i in range(a,b+1):
    t=i
    s=0
    while(i>0):
        r=i%10;
        s=s+r*r*r;
        i=i//10
    if(s==t):
        print("armstrong number:",t)
