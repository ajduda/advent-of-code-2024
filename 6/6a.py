file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

blockers = set()
y = 0

for line in z.split('\n'):
    x = 0
    for c in line:
        if c == '#':
            blockers.add((y,x))
        elif c == '^':
            guardX = x
            guardY = y
        x += 1
    maxX = x

    y += 1    

maxY = y
d = 1  # unit circle, 0 = right, 1 up, 2 left, 3 down


visited = {(guardY,guardX)}
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
        visited.add((guardY,guardX))

print(len(visited)-1)