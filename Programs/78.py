#convert first and last character of a string to upper case
s=input("enter a string:")
s=s.split(' ')
for i in s:
    l=len(i)
    print(i[0:1].upper()+i[1:l-1]+i[l-1:l].upper())
