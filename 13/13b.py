file = 'test.txt'
file = 'input.txt'

def lcm(a,b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    for i in range(big, big*small+1,big):
        if i % small == 0:
            return i

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

    #part B twist big numbers
    prizeX += 10000000000000
    prizeY += 10000000000000

    #find A,B such that 94*A+22*B = 8400 and 34*A+67*B = 5400
    """
    Ax*A + Bx*B = Px
    Ay*A + By*B = Py
    #  Google says Cramer's Rule just solves this, but I don't remember how to derive it so we're hacking this out via substitution

    Solve eq1 for A
    Ax*A = Px - Bx*b
    A = (Px - Bx*B)/Ax
    Plug A into eq2
    Ay(Px - Bx*B)/Ax + By*B = Py
    By*B = Py - Ay(Px - Bx*B)/Ax
    By*B = Py - Ay*Px/Ax + Ay*Bx*B/Ax
    By*B - Ay*Bx*B/Ax = Py - Ay*Px/Ax
    B(By - Ay*Bx/Ax) = Py - Ay*Px/Ax
    B(By*Ax - Ay*Bx)/Ax = (Py*Ax - Ay*Px)/Ax
    B = (Py*Ax - Ay*Px) / (By*Ax - Ay*Bx)
    Given B, plug into A = (Px - Bx*B)/Ax
    Check for integer coordinates
    """

    Px = prizeX
    Py = prizeY

    B = (Py*Ax - Ay*Px) / (By*Ax - Ay*Bx)
    A = (Px - Bx*B)/Ax

    if A == int(A) and B == int(B):
        ans += 3*A + B


print(int(ans))