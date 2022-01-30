#try except
n=input("enter a number:")
try:
    p=int(n)
except:
    p=-1
if(p>0):
    print("entered number is in numeric")
else:
    print("entered number is not in numeric")
