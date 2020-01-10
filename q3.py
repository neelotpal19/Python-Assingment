'''Python Assignment Q-3'''
INPUT_LIST = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
SET_INPUT_LIST = set(INPUT_LIST)
RESULT = []
for VALUE in INPUT_LIST:
    if VALUE in SET_INPUT_LIST:
        RESULT.append(VALUE)
        SET_INPUT_LIST.remove(VALUE)
print(RESULT)
