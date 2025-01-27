file,dim,steps = 'test.txt',6,12
file,dim,steps = 'input.txt',70,1024

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

blocks = set()
counter = 0
for line in z.split('\n'):
    y,x = line.split(',')
    y = int(y)
    x = int(x)
    blocks.add((y,x))
    counter += 1
    if counter >= steps:
        break

#BFS style flood fill
explorable = {(0,0)}
searched = set()

while (dim,dim) not in searched:
    nextExplorable = set()
    while len(explorable) > 0:
        (y,x) = explorable.pop()
        for (dy,dx) in [(1,0),(0,1),(-1,0),(0,-1)]:
            coord = (y+dy,x+dx)
            if x + dx < 0 or x + dx > dim or y + dy < 0 or y + dy > dim:
                continue
            if coord not in blocks and coord not in searched:
                nextExplorable.add(coord)
                searched.add((coord))
    explorable = nextExplorable
    ans += 1

print(ans)