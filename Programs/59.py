#palindrom in given range
l=int(input("enter lower bound:"))
u=int(input("enter upper bound:"))
for i in range(l,u):
    t=i
    s=0
    while(i>0):
        r=i%10
        s=s*10+r
        i=i//10
    if(s==t):
        print("palindrome:",t)
