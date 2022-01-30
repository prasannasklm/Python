#program to find whether the string contains atleast one digit or one character
s=input("enter a string:")
c=0
d=0
for i in s:
    if(i.isalpha()):
        c=c+1
    if(i.isdigit()):
        d=d+1
if(c>0 and d>0):
    print("string contains atleast one character and digit!!!")
    print("characters:",c)
    print("digits:",d)
else:
    print("either characters or digits less than zero")
