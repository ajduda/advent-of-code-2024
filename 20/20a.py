file = 'test.txt'
#file = 'input.txt'

#returns length of path using BFS
def BFS(start,end,walls,maxY,maxX):
    searched = set()
    explorable = {start}
    ret = 0
    while end not in searched:
        nextExplorable = set()
        while len(explorable) > 0:
            (y,x) = explorable.pop()
            for (dy,dx) in [(1,0),(0,1),(-1,0),(0,-1)]:
                coord = (y+dy,x+dx)
                if x + dx < 0 or x + dx >= maxX or y + dy < 0 or y + dy >= maxY:
                    continue
                if coord not in walls and coord not in searched:
                    nextExplorable.add(coord)
                    searched.add((coord))
        explorable = nextExplorable
        ret += 1
    return ret



with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0


walls = set()
y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == 'S':
            start = (y,x)
        if c == 'E':
            end = (y,x)
        if c == '#':
            walls.add((y,x))
        x += 1    
    y += 1

maxY = y
maxX = x
baseline = BFS(start,end,walls,maxY,maxX)

print(len(walls))
i = 0
for wall in walls:
    print(i)
    i += 1
    wallsTemp = walls.copy()
    wallsTemp.remove(wall)
    length = BFS(start,end,wallsTemp,maxY,maxX)
    diff = baseline - length
    if diff >= 100:
        ans += 1
print(ans)