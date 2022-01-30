# program to find whther entered letter is vowel or consonant
n=input("enter a letter:")
c=0
for i in n:
    c=c+1
if(c==1):
    if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
        print("enterd letter is vowel")
    else:
        print("entered letter is consonant")
else:
    print("please enter single letter only")
