#making half string upper
s=input("enter a string:")
l=(len(s)//2)-1
p=[]
for i in range(len(s)):
    if i>l:
        p+=s[i].upper()
    else:
        p+=s[i]
print(''.join(p))
