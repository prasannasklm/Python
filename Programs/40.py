#palindrome number
n=int(input("enter a number:"))
t=n
s=0
while (n>0):
    r=n%10
    s=(s*10)+r      #// floor division  / normal division
    n=n//10
    print(n)
if(t==s):
    print("PALINDROME!!")
else:
    print("NOT PALINDROME")
