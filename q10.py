'''Python Assignment Q-10'''
# pylint: disable=too-few-public-methods
class Reverselter:
    '''Reverselter Class'''
    def __init__(self, input_list):
        '''Constructor'''
        for i in reversed(range(len(input_list))):
            print(input_list[i])
LIST = [1, 2, 3, 4, 5]
Reverselter(LIST)
