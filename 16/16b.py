file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

grid = []
y = 0
for line in z.split('\n'):
    grid.append([])
    x = 0
    for c in line:
        grid[-1].append(c)
        if c == 'S':
            start = (y,x)
        if c == 'E':
            end = (y,x)
        x += 1    
    y += 1

#d = 0 is facing east, d is purpendicular to d+1
directions = [(0,1),(1,0),(0,-1),(-1,0)]

#stored as coordinates: direction
frontier = {start: 0}

#stored as coordinates: min score
score = {start: 0}
searched = set()

while end not in searched:
    bestCoord = None
    bestScore = None
    for k in frontier.keys():
        if bestCoord is None or score[k] < bestScore:
            bestCoord = k
            bestScore = score[k]
    d = frontier.pop(bestCoord)
    searched.add(bestCoord)
    myScore = score[bestCoord]
    (y,x) = bestCoord
    (dy,dx) = directions[d]
    nextCoord = (y+dy,x+dx)
    if nextCoord not in searched and grid[y+dy][x+dx] != '#':
        if nextCoord not in score or score[nextCoord] < myScore + 1:
            frontier[nextCoord] = d
            score[nextCoord] = myScore + 1
    #check purpendicular directions
    d += 1
    d %= 4
    (dy,dx) = directions[d]
    nextCoord = (y+dy,x+dx)
    if nextCoord not in searched and grid[y+dy][x+dx] != '#':
        if nextCoord not in score or score[nextCoord] < myScore + 1001:
            frontier[nextCoord] = d
            score[nextCoord] = myScore + 1001

    d -= 2
    d %= 4
    (dy,dx) = directions[d]
    nextCoord = (y+dy,x+dx)
    if nextCoord not in searched and grid[y+dy][x+dx] != '#':
        if nextCoord not in score or score[nextCoord] < myScore + 1001:
            frontier[nextCoord] = d
            score[nextCoord] = myScore + 1001

# We have the score of the final, DFS from start to search all paths, marking the tile if I could get there in the score    
winningCells = {end}
memoize = {}


def DFS(grid,y,x,d,scoreLimit,myScore):
    if (y,x,d,myScore) in memoize:
        return memoize[(y,x,d,myScore)]
    if myScore > scoreLimit:
        return False
    if (y,x) == end:
        return True
    global winningCells
    (dy,dx) = directions[d]
    myCellFinishes = False
    if grid[y+dy][x+dx] != '#':
        myCellFinishes |= DFS(grid,y+dy,x+dx,d,scoreLimit,myScore+1)
    d += 1
    d %= 4
    (dy,dx) = directions[d]
    if grid[y+dy][x+dx] != '#':
        myCellFinishes |= DFS(grid,y+dy,x+dx,d,scoreLimit,myScore+1001)
    d -= 2
    d %= 4
    (dy,dx) = directions[d]
    if grid[y+dy][x+dx] != '#':
        myCellFinishes |= DFS(grid,y+dy,x+dx,d,scoreLimit,myScore+1001)
    
    if myCellFinishes:
        winningCells.add((y,x))
    #reset d for memoization
    d += 1
    d %= 4
    memoize[(y,x,d,myScore)] = myCellFinishes
    return myCellFinishes


(y,x) = start
DFS(grid,y,x,0,score[end],0)

print(len(winningCells))