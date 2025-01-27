file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

start,code = z.split('\n\n')
lines = start.split('\n')
A = int(lines[0].split(': ')[1])
B = int(lines[1].split(': ')[1])
C = int(lines[2].split(': ')[1])

code = code.split(': ')[1]

program = []
for n in code.split(','):
    program.append(int(n))

instPtr = 0

ans = ""

while instPtr < len(program) and instPtr >= 0:
    opcode = program[instPtr]
    combo = program[instPtr+1]
    if 0 <= combo and combo <= 3:
        operand = combo
    elif combo == 4:
        operand = A
    elif combo == 5:
        operand = B
    elif combo == 6:
        operand = C
    else:
        pass
        #print('ERROR: operand was',combo)

    match opcode:
        case 0:  # adv
            A = A // (2**operand)
        case 1:  # bxl
            B ^= combo  # names are backwards, this is literal operand
        case 2:  # bst
            B = operand % 8
        case 3:  # jzn
            if A != 0:
                instPtr = combo  # names are backwards, this is literal operand
                instPtr -= 2  # offset the end incrementation
        case 4:  # bxc
            B ^= C
        case 5:  # out
            ans += str(operand%8)
            ans += ','
        case 6:  # bdv
            B = A // (2**operand)
        case 7:  # cdv
            C = A // (2**operand)
        case _:
            print('ERROR: instruction was',opcode)

    instPtr += 2

print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')

print(ans[:-1])