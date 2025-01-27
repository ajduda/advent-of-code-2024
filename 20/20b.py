file,threshold = 'test.txt',50
file,threshold = 'input.txt',100

# This is legacy from before I realized it's not a maze, but a twisty path. This has a silly bug I can't track down that 98% gets the answer but refactoring will be much easier

#returns length of path using BFS


with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0


space = set()
y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c == 'S':
            start = (y,x)
        if c == 'E':
            end = (y,x)
        if c != '#':
            space.add((y,x))
        x += 1    
    y += 1

coordPathIndex = {start: 0}
coord = start
index = 0
while end not in coordPathIndex:
    index += 1
    (y,x) = coord
    for (dy,dx) in [(1,0),(0,1),(-1,0),(0,-1)]:
        newCoord = (y+dy,x+dx)
        if newCoord not in coordPathIndex and newCoord in space:
            coordPathIndex[newCoord] = index
            coord = newCoord


saves = {}
for cheatStart in coordPathIndex:
    (y,x) = cheatStart
    for dy in range(-20,21):
        for dx in range(-20,21):
            manhattan = abs(dx) + abs(dy)
            if manhattan > 20:
                continue
            cheatEnd = (y+dy,x+dx)
            if cheatEnd not in space:
                continue
            savings = coordPathIndex[cheatEnd] - coordPathIndex[cheatStart] - manhattan
            if savings >= threshold:
                ans += 1


print(ans)
