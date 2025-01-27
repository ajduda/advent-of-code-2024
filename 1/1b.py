file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

left = {}
right = {}

def increment(d,i):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for line in z.split('\n'):
    l,r = line.split('   ')
    l = int(l)
    r = int(r)
    increment(left,l)
    increment(right,r)

print(left)
print(right)

for k in left.keys():
    if k in right:
        ans += k*left[k]*right[k]

print(ans)