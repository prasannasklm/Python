#continue
n=int(input("enter a number:"))
while(n>0):
    if(n%2==0):
        n=n-1;
        continue
    print(n)
    n=n-1
print("end of the program")
