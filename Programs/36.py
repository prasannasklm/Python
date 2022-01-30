##write a program that repeatedly takes an input from the user until the user enters "done". when user enters done we show the largest and smallest of the values that entered before. if the user takes invalid input it shows error
s=None
l=0
while True:
    n1=input("enter a value:")
    if(n1=="done"):
        print("largest:",l)
        print("smallest:",s)
        quit()
    else:
        try:
            n=int(n1)
            if(n>l):
                l=n
            if(s is None):
                s=n
            if(n<s):
                s=n
        except:
            print("invalid data")
