import random, time, copy
WIDTH = 60
HEIGHT = 20

#Import modules

nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0: 
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

#A list of lists must be created to store the two symbols used for the cellular automata. In this case '#' and ' '. "living" and "dead" cells. Where they are in the list reflects where they are posititioned on the screen. The inner list is for a column and the random.randint(0, 1) gives it a 50% chance of being alive or dead. 

#The nextCells variable contains our list of lists. x starts at 0 moving left to right and y starts at 0 moving down.

while True:
    print('\n\n\n\n\n') #Separate each step with new lines
    currentCells = copy.deepcopy(nextCells)

#After every iteration through the loop, nextCells is coppied to currentCells, and then currentCells is printed and then used again for the nextCells.

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

#The nested for loops above print a full row of currentCells on the screen breaking up each line with the "end='' command."

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT 

#The above for loop calculate each cell when printed. The state of the cell depends on the state of the cells around it. 

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.cl
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            
# the code above checks if every cell should be living or dead and the series of 'if' statements looks at each neighbor of the current cell. If the cell is "alive," 1 is added to the numNeighbors variable.

            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
        time.sleep(0.01)