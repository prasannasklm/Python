#break in while loop
n=int(input("enter a number:"))
while(n>0):
    if(n>=18):
        print("you are eligible for voting")
        break
    print(n)
    n=n-2
print("end of the program")
