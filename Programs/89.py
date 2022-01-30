l=['1','2','3','4','0']
leng=0
for i in l:
    leng=leng+1
print("length of list:",leng)
l1=[]
while(leng>0):
    l1+=l[leng-1]
    leng=leng-1
print(l1)
