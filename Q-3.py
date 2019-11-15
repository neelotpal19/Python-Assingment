l=[12,24,35,24,88,120,155,88,120,155]
s=set(l)
res=[]
for i in l:
    if(i in s):
        res.append(i)
        s.remove(i)
print(res)
