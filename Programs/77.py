#counting no.of vowels in a string
s=input("enter a string:")
c=0
for k in s:
    if(k=='a' or k=='e' or k=='i' or k=='o' or k=='u'):
        c=c+1
if (c>0):
    print("no.of vowels is the given string is:",c)
else:
    print("there are no vowels")    
