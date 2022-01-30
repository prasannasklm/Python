#functions
#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters ( hours and  rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
def totalpay(h,r):
    c=h-40
    print("total pay is:",40*r+c*1.5*r)
h=float(input("enter hours:"))
r=float(input("enter rate:"))
if(h>40):
    totalpay(h,r)
else:
    print("total pay is:",h*r)
