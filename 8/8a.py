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

print(maxX)
print(maxY)

antinodes = set()

for letter in antenna.keys():
    antennaList = antenna[letter]
    for i in range(len(antennaList)):
        for j in range(i+1,len(antennaList)):
            (y1,x1) = antennaList[i]
            (y2,x2) = antennaList[j]
            diffY = y2-y1
            diffX = x2-x1
            if y2 + diffY >= maxY or y2 + diffY < 0 or x2 + diffX >= maxX or x2 + diffX < 0:
                pass #node out of bounds
            else:
                if (y2+diffY,x2+diffX) not in antennaList:
                    antinodes.add((y2+diffY,x2+diffX))
            if y1 - diffY >= maxY or y1 - diffY < 0 or x1 - diffX >= maxX or x1 - diffX < 0:
                pass #node out of bounds
            else:
                if (y1-diffY,x1-diffX) not in antennaList:
                    antinodes.add((y1-diffY,x1-diffX))


print(antinodes)
print(len(antinodes))