file = 'test.txt'
file = 'input.txt'

def nextSecret(n):
    n ^= n << 6
    n %= 16777216
    n ^= n >> 5
    n %= 16777216
    n ^= n << 11
    n %= 16777216
    return n


with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    n = int(line)
    for i in range(2000):
        n = nextSecret(n)
    ans += n

print(ans)