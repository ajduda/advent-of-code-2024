file,height,width = 'test.txt',7,11
file,height,width = 'input.txt',103,101



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


for i in range(100):
    for robot in robots:
        vx,vy = robot[0]
        px = robot[1][0]
        py = robot[1][1]
        robot[1] = [(px+vx)%width, (py+vy)%height]

quads = [0,0,0,0]    


for robot in robots:
    quad = 0
    x = robot[1][0]
    y = robot[1][1]
    if x == (width // 2) or y == (height // 2):
        continue
    if x > (width // 2):
        quad += 2
    if y > (height // 2):
        quad += 1
    quads[quad] += 1

ans = 1
for n in quads:
    ans *= n

print(ans)