'''Python Assignment Q-9'''
import os
COUNT = 0
PATH = [r for r, d, folder in os.walk("H:\MY")]
def fun(s):
    '''Print the directories and files'''
    global count
    if(os.path.isdir(PATH[++COUNT])):
        print(os.listdir(s))
        if(COUNT == len(PATH)-1):
            return 0
        else:
            COUNT += 1
            fun(PATH[COUNT])
       
    else:
        print("No directory exist")
        return 0
function_call = fun("H:\MY")
