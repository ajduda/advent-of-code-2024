file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

blockersBaseline = set()
y = 0

for line in z.split('\n'):
    x = 0
    for c in line:
        if c == '#':
            blockersBaseline.add((y,x))
        elif c == '^':
            guardXStart = x
            guardYStart = y
        x += 1
    maxX = x

    y += 1    
maxY = y

for i in range(maxY):
    for j in range(maxX):
        if (i,j) in blockersBaseline:
            continue
        if i == guardYStart and j == guardXStart:  # oops, don't throw stuff on the guard
            continue
        #doing a shallow copy manually
        blockers = set()
        for coord in blockersBaseline:
            blockers.add(coord)
        blockers.add((i,j))
        guardY = guardYStart
        guardX = guardXStart
        d = 1  # start facing up # unit circle, 0 = right, 1 up, 2 left, 3 down
        print(f'starting iter on ({i},{j})')
        #visited = {(guardY,guardX,d)}
        visited = set()
        while guardX >= 0 and guardX < maxX and guardY >= 0 and guardY < maxY:
            if d == 0:
                dx = 1
                dy = 0
            if d == 1:
                dx = 0
                dy = -1
            if d == 2:
                dx = -1
                dy = 0
            if d == 3:
                dx = 0
                dy = 1
            if (guardY+dy,guardX+dx) in blockers:
                d -= 1
                d %= 4
            else:
                guardX += dx
                guardY += dy
                if (guardY,guardX,d) in visited: # loop found
                    ans += 1
                    #print(f'loop found when blocker added at coord ({i},{j})')
                    break
                else:
                    visited.add((guardY,guardX,d))


print(ans)