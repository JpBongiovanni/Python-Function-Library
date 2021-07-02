import random
numberOfStreaks = 0
H = 0
T = 0

for experimentNumber in range(10000):
    if random.randint(0,1) == 0:
        # print('H', end=" ")
        H = H + 1
        T = 0
        if H == 6:
            numberOfStreaks += 1
            H = 0 
    elif random.randint(0,1) == 1:
        # print('T', end=" ")
        T = T + 1
        H = 0
        if T == 6:
            numberOfStreaks += 1



print('Chance of streak: %s%%' % (numberOfStreaks / 100))