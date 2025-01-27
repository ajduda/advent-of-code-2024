file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

left = []
right = []

for line in z.split('\n'):
    l,r = line.split('   ')
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

for i in range(len(left)):
    ans += abs(left[i]-right[i])

print(ans)