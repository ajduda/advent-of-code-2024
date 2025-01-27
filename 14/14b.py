file,height,width = 'input.txt',103,101


#interesting thing between 1100 and 1125
#2648,2571
checkingStart = 0
checkingEnd = 7000

f = open('terminalOutput.txt','a')

def printGrid(locations):
    for y in range(height):
        s = ''
        for x in range(width):
            if (x,y) in locations:
                s += '*'
            else:
                s += ' '
        s += '\n'
        f.write(s)


with open(file) as inp:
    z = inp.read()
    z = z.strip()

robots = []

for line in z.split('\n'):
    sections = line.split('=')
    px = int(sections[1].split(',')[0])
    py = int(sections[1].split(',')[1].split('v')[0])
    vx = int(sections[2].split(',')[0])
    vy = int(sections[2].split(',')[1])

    robots.append([(vx,vy),[px,py]])


for i in range(1,checkingEnd):
    locations = set()
    for robot in robots:
        vx,vy = robot[0]
        px = robot[1][0]
        py = robot[1][1]
        locations.add((px,py))
        robot[1] = [(px+vx)%width, (py+vy)%height]
    if i > checkingStart:
        f.write(f'{i} iteration!\n')
        printGrid(locations)