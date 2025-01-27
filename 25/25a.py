file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

locks = set()
keys = set()

k = 0
l = 0

for block in z.split('\n\n'):
    if block[0] == '#':
        setToAdd = locks
    else:
        setToAdd = keys
    lines = block.split('\n')
    heights = []
    for c in range(5):
        height = 0
        for h in range(1,len(lines)-1):
            if lines[h][c] == '#':
                height += 1
        heights.append(height)
    setToAdd.add((tuple(heights)))


for (a1,a2,a3,a4,a5) in locks:
    for (b1,b2,b3,b4,b5) in keys:
        if a1 + b1 < 6 and a2 + b2 < 6 and a2 + b2 < 6 and a3 + b3 < 6 and a4 + b4 < 6 and a5 + b5 < 6:
            ans += 1

print(ans)