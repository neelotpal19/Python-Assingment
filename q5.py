'''Python Assignment Q-3'''
# pylint: disable=R1705
def binary_search(input_list, search_value):
    '''Function return the index of searched value'''
    first_value = 0
    last_value = len(input_list) - 1
    while last_value >= first_value:
        mid_value = int((first_value + last_value)/2)
        if input_list[mid_value] == search_value:
            return mid_value
        elif search_value > input_list[mid_value]:
            first_value = mid_value + 1
        else:
            last_value = mid_value - 1
INPUT_LIST_VALUE = [1, 5, 6, 8, 9, 10]
SEARCH = 10
OUTPUT = binary_search(INPUT_LIST_VALUE, SEARCH)
print(OUTPUT)
