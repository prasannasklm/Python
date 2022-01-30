# conditional statements example
# nested if statements
n=int(input("enter a number:"))
if(n>0):
    print("entered number is positive number...")
    if(n%2==0):
        print("entered number is even and positive")
    if(n%2!=0):
        print("entered number is odd and positive")
    print("exiting from inner if block")
print("exiting from outer if block")
if(n<0):
    print("enterd number is negative")
print("end of the program")
