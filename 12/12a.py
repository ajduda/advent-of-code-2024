file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

grid = [[]]

for line in z.split('\n'):
    grid.append(['-']) #ringed with dashes for ease
    for c in line:
        grid[-1].append(c)
    grid[-1].append('-')

grid.append([])

for _ in range(len(grid[1])):
    grid[0].append('-')
    grid[-1].append('-')

checked = set()
dirs = [(-1,0),(1,0),(0,-1),(0,1)]


for i in range(1,len(grid)-1):
    for j in range(1,len(grid[i])-1):
        if (i,j) not in checked:
            #flood fill sort of search
            checked.add((i,j))
            toCheck = {(i,j)}
            region = {(i,j)}
            regionLetter = grid[i][j]
            perimeter = 0
            while len(toCheck) > 0:
                coord = toCheck.pop()
                (y,x) = coord
                for (dy,dx) in dirs:
                    if (y+dy,x+dx) in region:
                        continue
                    if grid[y+dy][x+dx] != regionLetter:
                        perimeter += 1
                    else:
                        region.add((y+dy,x+dx))
                        checked.add((y+dy,x+dx))
                        toCheck.add((y+dy,x+dx))
            ans += len(region) * perimeter

print(ans)