#printing strings that have all vowels
s=input("enter a string:")
a=0
e=0
i=0
o=0
u=0
for k in s:
    if(k=='a'):
        a=1
    elif(k=='e'):
        e=1
    elif(k=='i'):
        i=1
    elif(k=='o'):
        o=1
    elif(k=='u'):
        u=1
if(a==1 and e==1 and i==1 and o==1 and u==1):
    print(s,"is accepted as it contains all the vowels")
else:
    print("string not accepted")
