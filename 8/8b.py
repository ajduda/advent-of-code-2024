file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0
antenna = {}


y = 0
for line in z.split('\n'):
    x = 0
    for c in line:
        if c != '.' and c != '#':
            if c in antenna:
                antenna[c].append((y,x))
            else:
                antenna[c] = [(y,x)]
        x += 1
    maxX = x
    y += 1
maxY = y

antinodes = set()

for letter in antenna.keys():
    antennaList = antenna[letter]
    if len(antennaList) == 1:
        continue
    for i in range(len(antennaList)):
        antinodes.add((antennaList[i]))
        for j in range(i+1,len(antennaList)):
            (y1,x1) = antennaList[i]
            (y2,x2) = antennaList[j]
            diffY = y2-y1
            diffX = x2-x1
            while y2 + diffY < maxY and y2 + diffY >= 0 and x2 + diffX < maxX and x2 + diffX >= 0:
                y2 += diffY
                x2 += diffX
                antinodes.add((y2,x2))
            while y1 - diffY < maxY and y1 - diffY >= 0 and x1 - diffX < maxX and x1 - diffX >= 0:
                y1 -= diffY
                x1 -= diffX
                antinodes.add((y1,x1))

for y in range(maxY):
    s = ''
    for x in range(maxX):
        if (y,x) in antinodes:
            s += '#'
        else:
            s += '.'
    print(s)

print(antinodes)

print(len(antinodes))