file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

initialValues, instrs = z.split('\n\n')

setWires = {}

for line in initialValues.split('\n'):
    l,r = line.split(': ')
    setWires[l] = int(r)

wires = set()

for line in instrs.split('\n'):
    l,r = line.split(' -> ')
    l1,inst,l2 = l.split(' ')
    wires.add((l1,l2,inst,r))

while len(wires) > 0:
    wiresToRemove = set()
    for wire in wires:
        (l1,l2,inst,r) = wire
        if l1 in setWires and l2 in setWires:
            match inst:
                case 'OR':
                    setWires[r] = setWires[l1] | setWires[l2]
                case 'XOR':
                    setWires[r] = setWires[l1] ^ setWires[l2]
                case 'AND':
                    setWires[r] = setWires[l1] & setWires[l2]
                case _:
                    print('ERROR: inst was', inst)
            wiresToRemove.add(wire)
    for wire in wiresToRemove:
        wires.remove(wire)

ans = 0
i = 0
n = 1
s = 'z00'
while s in setWires:
    ans += n*setWires[s]
    n *= 2
    i += 1
    s = 'z'
    if i < 10:
        s += '0'
    s += str(i)

print(ans)