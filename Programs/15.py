#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input
h=input("enter hours:")
r=input("enter rate:")
try:
    hrs=float(h)
    rate=float(r)
except:
    print("please enter the data in numeric format...")
    quit()
if(hrs>40):
    c=hrs-40
    print("total pay is:",40*rate+c*1.5*rate)
else:
    print("total pay is:",hrs*rate)
