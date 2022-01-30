#select the words which has upper case as starting letter
s=input("enter a string:")
s=s.split(' ')
for i in s:
    if(i[0].isupper()):
        print(i)
