#write a program that repeatedly takes an input from the user until the user enters "done". when user enters done we show the sum of the values that entered before. if the user takes invalid input it shows error
s=0
c=0
while True:
    n1=input("enter a number:")
    if(n1=="done"):
        print("sum,count,avg:",s,c,s/c)
        quit()
    else:
        try:
            n=int(n1)
            s=s+n;
            c=c+1;
        except:
            print("invalid input")
