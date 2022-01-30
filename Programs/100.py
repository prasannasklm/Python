#tuples
tu=()
print(tu)
t1=(2,4,1,7,8,4)
print(t1)
print(t1.count(4))
print(t1.count(2))
print("index:",t1.index(1))
(a,b)=(1,"two")
print((a,b))
print(a)
print(b)
dic={"one":4,"two":3,"four":2}
for i,j in dic.items():
    print((i,j))
t=dic.items()
print(t)
print(sorted(dic.items()))
