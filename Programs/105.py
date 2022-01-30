import re
s="http://www.ssc.gov.in and https://www.facebook.com"
m=re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
match=m.findall(s)
print(match)
