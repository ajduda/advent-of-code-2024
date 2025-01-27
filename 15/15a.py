file = 'test.txt'
file = 'input.txt'


#returns (coordinate, canMove)
def tryMoving(walls,boxes,move,coord):
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
        return (coord, False)
    
    elif newCoord in boxes:
        shove = tryMoving(walls,boxes,move,newCoord)
        if shove[1]:
            boxes.remove(newCoord)
            newBoxCoord = (y+dy+dy,x+dx+dx)
            boxes.add(newBoxCoord)
            return (newCoord,True)
        else:
            return(coord, False)
    
    else:
        return (newCoord,True)
    
    print('ERROR')
    exit()

with open(file) as inp:
    z = inp.read()
    z = z.strip()

sections = z.split('\n\n')
blocks = sections[0]
moves = sections[1]

walls = set()
boxes = set()

y = 0
for line in blocks.split('\n'):
    x = 0
    for c in line:
        if c == '@':
            robot = (y,x)
        elif c == 'O':
            boxes.add((y,x))
        elif c == '#':
            walls.add((y,x))
        x += 1
    y += 1

for line in moves.split('\n'):
    for move in line:
        robot = tryMoving(walls,boxes,move,robot)[0]

ans = 0

for coord in boxes:
    (y,x) = coord
    ans += (100*y) + x

print(ans)