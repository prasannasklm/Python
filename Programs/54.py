#roots of quadratic equation
import math
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b*b)-(4*a*c)
if(d>0):
    print("root 1:",(-b+math.sqrt(d))/(2*a))
    print("root 2:",(-b-math.sqrt(d))/(2*a))
elif(d==0):
    print("roots are equal:",(-b/(2*a)))
elif(d<0):
    print("root 1:",(-b/(2*a)),"+",math.sqrt(-d)/(2*a),"i")
    print("root 2:",(-b/(2*a)),"-",math.sqrt(-d)/(2*a),"i")
