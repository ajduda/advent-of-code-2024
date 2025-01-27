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
dirs = [(-1,0),(0,-1),(1,0),(0,1)]  #rearranged dirs for part b so I can know dirs[n] is orthogonal to dirs[(n+1)%4]


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '-':
            continue
        if (i,j) not in checked:
            #flood fill sort of search
            checked.add((i,j))
            toCheck = {(i,j)}
            region = {(i,j)}
            regionLetter = grid[i][j]
            perimeter = set()
            while len(toCheck) > 0:
                coord = toCheck.pop()
                (y,x) = coord
                for d in range(len(dirs)):
                    (dy,dx) = dirs[d]
                    if (y+dy,x+dx) in region:
                        continue
                    if grid[y+dy][x+dx] != regionLetter:
                        perimeter.add((d,(y+dy,x+dx)))
                    else:
                        region.add((y+dy,x+dx))
                        checked.add((y+dy,x+dx))
                        toCheck.add((y+dy,x+dx))
            #determine sides from perimeter set
            sides = 0
            while len(perimeter) > 0:
                (d,(y,x)) = perimeter.pop()
                sides += 1
                (dy,dx) = dirs[(d+1)%4]
                n = 1
                while (d,(y+(n*dy),x+(n*dx))) in perimeter:
                    perimeter.remove((d,(y+(n*dy),x+(n*dx))))
                    n += 1
                #check other direction
                (dy,dx) = dirs[(d-1)%4]
                n = 1
                while (d,(y+(n*dy),x+(n*dx))) in perimeter:
                    perimeter.remove((d,(y+(n*dy),x+(n*dx))))
                    n += 1 

            #print(f'REGION {regionLetter} has price {len(region) * sides}')
            ans += len(region) * sides

#print(len(checked))
#print(checked)

print(ans)