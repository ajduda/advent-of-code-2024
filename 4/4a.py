file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

grid = []

for line in z.split('\n'):
    grid.append([])
    for c in line:
        grid[-1].append(c)
    
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != 'X':
            continue
        #check right
        if x + 3 < len(grid[y]):
            dx = 1
            dy = 0
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check left
        if x - 3 >= 0:
            dx = -1
            dy = 0
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check up
        if y - 3 >= 0:
            dx = 0
            dy = -1
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check down
        if y + 3 < len(grid):
            dx = 0
            dy = 1
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check up right
        if y - 3 >= 0 and x + 3 < len(grid[y]):
            dx = 1
            dy = -1
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check down right
        if y + 3 < len(grid) and x + 3 < len(grid[y]):
            dx = 1
            dy = 1
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check down left
        if y + 3 < len(grid) and x - 3 >= 0:
            dx = -1
            dy =  1
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
        #check up left
        if y - 3 >= 0 and x - 3 >= 0:
            dx = -1
            dy = -1
            if grid[y][x] == 'X' and grid[y+dy][x+dx] == 'M' and grid[y+(2*dy)][x+(2*dx)] == 'A' and grid[y+(3*dy)][x+(3*dx)] == 'S':
                ans += 1
print(ans)