#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.Enter Hours: 45 Enter Rate: 10 #475 = 40 * 10 + 5 * 15
h=float(input("enter hours:"))
r=float(input("enter rate:"))
if(h>40):
    c=h-40
    print("total pay is:",40*r+c*1.5*r)
else:
    print("total pay is:",h*r)
