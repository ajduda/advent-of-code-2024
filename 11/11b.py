file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

stones = {}

def addToDict(d,n,count=1):
    if n in d:
        d[n] += count
    else:
        d[n] = count

for line in z.split('\n'):
    for n in line.split():
        num = int(n)
        addToDict(stones,num)

for i in range(75):
    newStones = {}
    for num in stones.keys():
        count = stones[num]
        if num == 0:
            addToDict(newStones,1,count)
        elif len(str(num)) % 2 == 0:
            s = str(num)
            l = s[:len(s)//2]
            r = s[len(s)//2:]
            addToDict(newStones,int(l),count)
            addToDict(newStones,int(r),count)
        else:
            addToDict(newStones,num*2024,count)
    stones = newStones

#print(stones)

ans = 0
for k in stones.keys():
    ans += stones[k]

print(ans)
