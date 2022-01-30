#creating dictionary from list
lis=[]
k=0
while(k<5):
    n=input("enter a name:")
    lis.append(n)
    k=k+1
print(lis)
dic={}
#l2=[]
for i in lis:
    '''if i not in l2:
        l2.append(i)
        dic[i]=1
    else:
        dic[i]=dic[i]+1'''
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)
'''for i in lis:
    dic[i]=dic.get(i)+1
print(dic)'''
for i in dic:
    print(i,dic[i])
print(dic.items())
print(dic.keys())
print(dic.values())
