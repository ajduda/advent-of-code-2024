file,dim = 'test.txt',6
file,dim = 'input.txt',70

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

blocksList = []

for line in z.split('\n'):
    y,x = line.split(',')
    y = int(y)
    x = int(x)
    blocksList.append((y,x))





blocks = set()
for block in blocksList:
    blocks.add(block)
    #BFS style flood fill
    explorable = {(0,0)}
    searched = set()

    while (dim,dim) not in searched and len(explorable) > 0:
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

    if (dim,dim) not in searched:
        print(block)
        exit()