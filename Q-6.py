def divide(n):
    l=[]
    for i in range(1,n+1):
        if(i%5==0 and i%7==0):
            yield(i)
l=divide(100)
print(tuple(l))
