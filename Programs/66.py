#palindrome
a=input("enter a string:")
length=len(a)
s=0
e=length-1;
p=1
if(length%2 ==0):
    print("even length string!!")
    while((s+1)!=e):
        if(a[s]==a[e]):
            s=s+1
            e=e-1
        else:
            p=0
            print("not palindrome!!")
            break
elif(length%2!=0):
    print("odd length string!!")
    while(s!=e):
        if(a[s]==a[e]):
            s=s+1
            e=e-1
        else:
            p=0
            print("not palindrome!!")
            break
if(p==1):
    print("palindrome!!!!")
