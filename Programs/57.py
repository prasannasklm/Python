#finding power of a number with out using inbuilt power function
b=int(input("enter base:"))
e=int(input("enter exponent"))
c=1
while(e>0):
    c=c*b 
    e=e-1
print("power is:",c)
