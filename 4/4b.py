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
    
for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        if grid[y][x] != 'A':
            continue
        vertical = False
        horizontal = False
        positiveDiag = False
        negativeDiag = False

        if grid[y+1][x] == 'M' and grid[y-1][x] == 'S':
            vertical = True
        if grid[y-1][x] == 'M' and grid[y+1][x] == 'S':
            vertical = True
        if grid[y][x+1] == 'M' and grid[y][x-1] == 'S':
            horizontal = True
        if grid[y][x-1] == 'M' and grid[y][x+1] == 'S':
            horizontal = True
        if grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S':
            positiveDiag = True
        if grid[y+1][x+1] == 'M' and grid[y-1][x-1] == 'S':
            positiveDiag = True
        if grid[y+1][x-1] == 'M' and grid[y-1][x+1] == 'S':
            negativeDiag = True
        if grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S':
            negativeDiag = True
        
        if vertical and horizontal:
            #ans += 1  # Oops, we don't accept +-Mas, only X-mas
            print('HORZ')
            print(f'({y},{x})')
        if positiveDiag and negativeDiag:
            ans += 1
            print('DIAG')
            print(f'({y},{x})')
        

print(ans)