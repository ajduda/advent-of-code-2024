file = 'test.txt'
file = 'input.txt'


def checkMove(walls,boxesL,boxesR,move,coord):
    (y,x) = coord
    if move == '^':
        dy = -1
        dx = 0
    elif move == '>':
        dy = 0
        dx = 1
    elif move == 'v':
        dy = 1
        dx = 0
    elif move == '<':
        dy = 0
        dx = -1
    else:
        print('ERROR: move was', move)
        exit()


    newCoord = (y+dy,x+dx)
    
    if newCoord in walls:
        return False

    if newCoord not in boxesL and newCoord not in boxesR:
        return True

    if move == '>' or move == '<':  #horizontal shifts are easy, check along entire route for gaps
        x += dx
        while (y,x) in boxesL or (y,x) in boxesR:
            x += dx
        if (y,x) in walls:
            return False
        else:
            return True

    #hitting a box going up or down
    else:
        if newCoord in boxesL:
            otherNewCoord = (y+dy,x+dx+1)
        else:
            otherNewCoord = (y+dy,x+dx-1)
        return checkMove(walls,boxesL,boxesR,move,newCoord) and checkMove(walls,boxesL,boxesR,move,otherNewCoord)

#Walls are irrelevent since we know the move is legal
def doMove(boxesL,boxesR,move,coord):
    (y,x) = coord
    if move == '^':
        dy = -1
        dx = 0
    elif move == '>':
        dy = 0
        dx = 1
    elif move == 'v':
        dy = 1
        dx = 0
    elif move == '<':
        dy = 0
        dx = -1
    else:
        print('ERROR: move was', move)
        exit()


    retCoord = (y+dy,x+dx)

    if move == '>':
        if retCoord in boxesL:
            newCoord = (y,x+2)
            # Shove along further boxes
            doMove(boxesL,boxesR,move,newCoord) 
            # Shove this box
            boxesL.remove(retCoord)
            boxesL.add(newCoord)
            boxesR.remove(newCoord)
            boxesR.add((y,x+3))
                
    elif move == '<':
        if retCoord in boxesR:
            newCoord = (y,x-2)
            # Shove along further boxes
            doMove(boxesL,boxesR,move,newCoord) 
            # Shove this box
            boxesR.remove(retCoord)
            boxesR.add(newCoord)
            boxesL.remove(newCoord)
            boxesL.add((y,x-3))

    # Vertical case
    else:
        if retCoord in boxesL or retCoord in boxesR:
            if retCoord in boxesL:
                otherBoxCoord = (y+dy,x+1)
                doMove(boxesL,boxesR,move,retCoord)
                doMove(boxesL,boxesR,move,otherBoxCoord)
                boxesL.remove(retCoord)
                boxesL.add((y+dy+dy,x))
                boxesR.remove(otherBoxCoord)
                boxesR.add((y+dy+dy,x+1))
            else:
                otherBoxCoord = (y+dy,x-1)
                doMove(boxesL,boxesR,move,retCoord)
                doMove(boxesL,boxesR,move,otherBoxCoord)
                boxesR.remove(retCoord)
                boxesR.add((y+dy+dy,x))
                boxesL.remove(otherBoxCoord)
                boxesL.add((y+dy+dy,x-1))

    #always return coordinate. If I'm a box, the return is ignored
    return retCoord

# For checking the example which didn't have an answer
def printGrid(walls,boxesL,boxesR,robot):
    for y in range(8):
        s = ''
        for x in range(16):
            if (y,x) in walls:
                s += '#'
            elif (y,x) in boxesL:
                s += '['
            elif (y,x) in boxesR:
                s += ']'
            elif (y,x) == robot:
                s += '@'
            else:
                s += '.'
        print(s)


with open(file) as inp:
    z = inp.read()
    z = z.strip()

sections = z.split('\n\n')
blocks = sections[0]
moves = sections[1]

walls = set()
boxesL = set()
boxesR = set()

y = 0
for line in blocks.split('\n'):
    x = 0
    for c in line:
        if c == '@':
            robot = (y,x)
        elif c == 'O':
            boxesL.add((y,x))
            boxesR.add((y,x+1))
        elif c == '#':
            walls.add((y,x))
            walls.add((y,x+1))
        x += 2
    y += 1


#print('starting grid')
#printGrid(walls,boxesL,boxesR,robot)
for line in moves.split('\n'):
    for move in line:
        if checkMove(walls,boxesL,boxesR,move,robot):
            robot = doMove(boxesL,boxesR,move,robot)
            #print('we moved',move)
            #printGrid(walls,boxesL,boxesR,robot)
        else:
            pass
            #print('we did not move',move)
ans = 0

for coord in boxesL:
    (y,x) = coord
    ans += (100*y) + x

print(ans)