file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

hardDrive = []
block = 0
writing = True

for line in z.split('\n'):
    for c in line:
        if writing:
            for i in range(int(c)):
                hardDrive.append(block)
        else:
            for i in range(int(c)):
                hardDrive.append(-1)
        writing = not writing
        if writing:
            block += 1

lptr = 0
rptr = len(hardDrive)-1

while lptr < rptr:
    while hardDrive[lptr] != -1:
        lptr += 1
    while hardDrive[rptr] == -1:
        rptr -= 1
    if lptr < rptr:
        hardDrive[lptr] = hardDrive[rptr]
        hardDrive[rptr] = -1

i = 0
while hardDrive[i] != -1:
    ans += i*hardDrive[i]
    i += 1

print(ans)