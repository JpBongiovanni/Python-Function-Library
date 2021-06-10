allGuests = {'Jason': {'lasagna': 4, 'bread sticks': 12},
            'Rocco': {'ham sandwiches': 3, 'meatballs': 4},
            'Dyanne': {'dishes': 3, 'cups': 1}
            }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        return numBrought

print('Number of things being brought:')
print(' - Lasagna        ' + str(totalBrought(allGuests, 'lasagna')))  
print(' - Bread Sticks   ' + str(totalBrought(allGuests, 'bread sticks'))) 
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches'))) 
print(' - Meatballs      ' + str(totalBrought(allGuests, 'meatballs'))) 
print(' - Dishes         ' + str(totalBrought(allGuests, 'dishes'))) 
print(' - Cups           ' + str(totalBrought(allGuests, 'cups'))) 