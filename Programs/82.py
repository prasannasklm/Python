import re
t=1
p=input("Enter a password:")
if(not(re.search('[a-z]',p))):
    t=0
if(not(re.search('[A-z]',p))):
    t=0
if(not(re.search('[0-9]',p))):
    t=0
if(not(re.search('[$@#!]',p))):
    t=0
if(len(p)<6 or len(p)>16):
    t=0
if(t==1):
    print ('Password is valid')
else:
    print ('Password is invalid')
