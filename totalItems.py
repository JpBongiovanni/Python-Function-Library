allGuests = {'Jason': {'lasagna': 4, 'bread sticks': 12},
            'Rocco': {'ham sandwiches': 3, 'meatballs': 4},
            'Dyanne': {'dishes': 10, 'cups': 10}
            }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.item():
        numBrought = numBrought + v.get(item, 0)
        return numBrought