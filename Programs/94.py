h=open("94.txt",'r')
for i in h:
    print(i)
c=0
for line in h:
    c=c+1
print("no.of lines in the text is:",c)
k=h.read()
print("length of the file is:",len(k))
f=open("94.txt",'r')
for i in f:
    print(i)
    if i.startswith("components"):
        print(i)
