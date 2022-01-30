s=input("enter a string:")
dictionary={}
l=s.split()
for i in l:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)
