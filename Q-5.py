import math
def binary(l,val):
    first=0
    last=len(l)-1
    while(last>=first):
        mid=int((first+last)/2)
        if(l[mid]==val):
            return mid
        elif(val>l[mid]):
            first=mid+1
        else:
            last=mid-1
l=[1,5,6,8,9,10]
val=10
i=binary(l,val)
print(i)
