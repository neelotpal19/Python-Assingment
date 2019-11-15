import os
count=0
l=[r for r, d, folder in os.walk("H:\MY")]
def fun(s):
    global count
    if(os.path.isdir(l[++count])):
        print(os.listdir(s))
        if(count==len(l)-1):
            return 0
        else:
            count+=1
            fun(l[count])
       
    else:
        print("No directory exist")
        return 0
a=fun("H:\MY")
