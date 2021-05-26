
# def commaCode(list):
#     for x in range(len(list)-1):
#         print(list[x] + ",", end= " ", sep=', ')

# commaCode(['apples', 'bananas', 'tofu', 'cats'])

# def commaCode(list):
#     print(*range(len(list)), sep=", ")

# commaCode(['apples', 'bananas', 'tofu', 'cats'])

def commaCode(list):
    for x in range(len(list)-1):
        print(list[x] + ",", end= " ", sep=', ') 

    # test = ''.join(list[:(len(list))-1])
    test2 = ''.join(list[(len(list))-1:])
    print('and ' + test2)

commaCode(['apples', 'bananas', 'tofu', 'cats', 'elephants', 'zebras', 'monkies'])
