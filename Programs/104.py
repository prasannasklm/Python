import re
s="s170191@rguktsklm.ac.in is the email and n180239@rguktn.ac.in o120134@rgkto.ac.in and also r130192@rguktrkv.ac.in and npn@gmail.com" #s170191@rguktsklm.ac.in
if(s):
    m=re.compile(r'[A-Za-z0-9]+@[a-z]+\.ac\.in')
    match=m.findall(s)
    print(match)
if(s):
    o=""
    k=re.compile(r'[A-Za-z0-9]+@[a-z]+\.com')
    p=k.findall(s)
    for i in p:
        o+=i
    if(len(o)==0):
            print(match)
            exit()
    match.append(o)
print(match)
