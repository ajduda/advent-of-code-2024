file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for block in z.split('\n\n'):
    lines = block.split('\n')
    A = lines[0].split('+')
    Ax = int(A[1].split(',')[0])
    Ay = int(A[2])
    B = lines[1].split('+')
    Bx = int(B[1].split(',')[0])
    By = int(B[2])
    prize = lines[2].split('=')
    prizeX = int(prize[1].split(',')[0])
    prizeY = int(prize[2])

    skip = False

    for a in range(101):
        if skip:
            break
        for b in range(101):
            if a*Ax + b*Bx == prizeX and a*Ay + b*By == prizeY:
                ans += a*3 + b
                skip = True
                break

print(ans)