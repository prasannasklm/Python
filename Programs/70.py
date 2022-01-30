#calculating characters without spaces
a=input("enter a sentence:")
p=[]
u=0
for i in a:
    if(i==' '):
        continue
    else:
        p+=i
        u=u+1
print(''.join(p))
print("no.of characters except spaces are:",u)
