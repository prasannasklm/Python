#looping through strings
print("looping through for loop")
a=input("enter a string:")
for i in a:
    print(i)
print("now looping through while loop")
b=input("enter a string:")
index=0
while index<len(b):
    print(b[index])
    index=index+1
print("looping and counting:")
count=0
for i in a:
    if(i=='a'):
        count=count+1
print("no.of a's in entered string is:",count)
print("slicing of the string is:",a[0:5])
print("slicing of the string is:",a[1:4])
print("hello"+"there")
print("hello"+" "+"there")
#in as logical operator
print('a' in "prasanna")
print('b' in "prasanna")
if('a' in "prasanna"):
    print("yeyyy!! fount it")
k=input("enter a letter to check:")
l=input("enter a string to check")
if(k in l):
    print("yeyy!! found it...")
else:
    print("mmmuu! not found")
