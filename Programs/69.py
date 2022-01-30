#removing ith character in a string
a=input("enter a string:")
d=int(input("enter i'th place to remove i'th character:"))
ne=[]
iny=0
length=len(a)
if(d > length):
    print("please enter valid i'th place....")
else:
    for i in a:
        if(iny==d):
            iny=iny+1;
            continue
        else:
            ne+=a[iny]
            iny=iny+1
print(''.join(ne))
