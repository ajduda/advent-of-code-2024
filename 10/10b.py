file = 'test.txt'
file = 'input.txt'

dirs = [(1,0),(-1,0),(0,1),(0,-1)]


def search(grid,y,x):
    if grid[y][x] == 9:
        #grid[y][x] = -1
        return 1
    
    possiblePaths = 0

    n = grid[y][x]
    for (dy,dx) in dirs:
        if grid[y+dy][x+dx] == (n + 1):
            possiblePaths += search(grid,y+dy,x+dx)

    return possiblePaths

    


with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

heights = [[]]

for line in z.split('\n'):
    heights.append([-1])
    for c in line:
        if c.isdigit():
            heights[-1].append(int(c))
        else:
            heights[-1].append(-1)
    heights[-1].append(-1)

heights.append([])
for i in range(len(heights[1])):
    heights[0].append(-1)
    heights[-1].append(-1)

for y in range(len(heights)):
    for x in range(len(heights[y])):
        if heights[y][x] == 0:
            #copy the grid so search can be destructive
            grid = []
            for line in heights:
                grid.append(line.copy())
                
            ans += search(grid,y,x)


print(ans)