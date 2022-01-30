#swapping without using 3rd variable
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("before swapping a and b are:",a,b)
a=a+b;
b=a-b
a=a-b
print("after swapping a and b are:",a,b)
