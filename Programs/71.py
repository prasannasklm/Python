#find even length words
#find even length words
a=input("enter a string:")
a=a.split(' ')
for i in a:
    if(len(i)%2==0):
        print(i)
