#multiway conditional statements
n=int(input("enter a number:"))
if(n<0):
    print("very small")
elif(n<10):
    print("small")
elif(n<100):
    print("medium")
elif(n<1000):
    print("large")
else:
    print("very large")
print("last line in the program")
