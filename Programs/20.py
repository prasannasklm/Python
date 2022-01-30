#functions
def fun(a):
    a=a*2
    return a
try:
    n=int(input("enter a number:"))
except:
    print("enter data in numeric form only")
    quit()
y=fun(n)+10
print(y)
