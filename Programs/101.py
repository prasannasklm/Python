#list comprehensions
h="hello world"
nl=[i for i in h]
print(nl)
nl1=[i for i in range(20) if i%2==0]
print(nl1)
nl2=[i for i in range(20) if i%2!=0]
print(nl2)
nl3=[i for i in range(20) if i%2==0 if i%5==0]
print(nl3)
