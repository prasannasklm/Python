#lists
a=[1,2,4,5]
for i in a:
    print(i)
b=[1,2,5,'p']
for j in b:
    print(j)
c=[1,2,3,'p',[4,5],9]
for k in c:
    print(k)
d=['prasanna','avinash','sri','narayana']
for i in d:
    print("hello",i)
print(d[0])
d[1]='avina'
print(d)
print("length:",len(d))
print(a+b)
print(d[1:4])
print(d[0:2])
print(d[1:])
print(d[:3])
v=[]
v.append(10)
v.append(20)
v.append('prasa')
print(v)
v.remove('prasa')
print(v)
v.sort()
print(v)
print(v.pop(1))
print(v)
print(max(a))
print(min(a))
print(sum(a))
