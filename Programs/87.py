#print unique words which have length greater than entered digit
s=input("enter a string:")
n=int(input("enter an integer:"))
p=s.lower()
k=p.split()
print(p)
print(k)
o=[]
l=[]
w=[]
x=[]
for i in k:
    c=0
    for j in k:
        if(i==j):
            c=c+1
    if(c==1):
        o+=i
        o+=' '
print(o)
u=''.join(o)
print(u)
m=u.split()
for i in m:
    if(len(i)>=n):
        l+=i
        l+=' '
print(''.join(l))
'''for r in p:
    for t in u:
        if(r==t):
            x+=r
        if(r==' '):
            x+=' '
print(x)'''
