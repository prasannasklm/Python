#symmetrical
a=input("enter a string:")
length=len(a)
p=1
s=0
e=length-1
mid=length//2
print(mid)
m=mid
while(s<mid and m<=e):
    if(a[s]==a[m]):
        s=s+1
        m=m+1
    else:
        p=0
        print("not symmetrical!!")
        break;
if(p==1):
    print("symmetrical!!")
