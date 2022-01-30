n=input()
l=[]
l=n.split()
print(l)
l.reverse()
print(l)
c=0
for i in l:
    for j in i:
        if(j=='"'):
            continue
        else:
            c=c+1
    break
print(c)
