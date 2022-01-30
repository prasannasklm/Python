#reverse a string
a=input("enter a string:")
#ne=[]
#i=len(a)
#while(i>0):
#    ne+=a[i-1]
#    i=i-1
#print("reversed string is:",ne)
l=len(a)
d=l-1
while(d>=0):
    print(a[d],end=""); #end uses to print the next letter in same line
    d=d-1
