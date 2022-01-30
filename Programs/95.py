k=input("enter a file:")
try:
    h=open(k)
except:
    print("file not available!!")
    quit()
r=h.read()
print(r)
c=0
print("length:",len(r))
for i in r:
    c=c+1
print(c)
