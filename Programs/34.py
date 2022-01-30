#iterations
#min
s=None
for i in [4,7,1,9,7,3]:
    if(s==None):
        s=i
    else:
        if(i<s):
            s=i;
print("min is:",s)
