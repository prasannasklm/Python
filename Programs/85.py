l=['1','4','5','7','9','2','3','11']
c=0
for i in l:
    k=int(i)
    cou=0
    for j in range(1,k+1):
        if(k%j==0):
            cou=cou+1
    if(cou==2):
        c=c+1
print("count of prime numbers:",c)
if(c<len(l)/4):
    print(1)
if(c>len(l)/4 and c<len(l)/2):
    print(2)
if(c>len(l)/2):
    print(3)    
