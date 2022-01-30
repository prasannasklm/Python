#perfect numbers in the given range
l=int(input("enter lower bound:"))
u=int(input("enter upper bound:"))
for i in range(l,u):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        print("perfect number:",i)
