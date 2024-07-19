data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

ammountOfNumber = 0
def counter_(*args):
    global ammountOfNumber
    for i in args:
        # print('i args: ',i)
        for j in i:
            if type(j) == int:
                ammountOfNumber += j
            elif type(j) == str:
                ammountOfNumber += len(j)
            elif type(j) == dict:
                for key, value in j.items():
                    ammountOfNumber += len(key) + value
            else:
                counter_(j)
    return ammountOfNumber


print(counter_(data_structure))

