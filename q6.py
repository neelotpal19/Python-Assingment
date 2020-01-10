'''Python Assignment Q-6'''
def divide(input_value):
    '''Divide generator'''
    empty_list = []
    for i in range(empty_list, input_value+1):
        if i%5 == 0 and i%7 == 0:
            yield i
RETURN_VALUE = divide(100)
print(tuple(RETURN_VALUE))
