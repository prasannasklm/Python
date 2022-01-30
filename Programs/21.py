#functions
def fun():
    print("your age is greater than or equal to 18!!\nyou are eligible for voting")
n=int(input("enter a number:"))
if(n>=18):
    fun()
else:
    print("function isn't invoked!!!\nnot eligible for the vote")
