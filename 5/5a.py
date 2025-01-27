file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

#  Order[x] = y means that x must come before y if they both exist
order = {}

for line in z.split('\n\n')[0].split('\n'):
    a,b = line.split('|')

    x = int(a)
    y = int(b)
    if x in order:
        order[x].add(y)
    else:
        order[x] = {y}

for line in z.split('\n\n')[1].split('\n'):
    elems = line.split(',')
    nums = []
    valid = True
    for s in elems:
        nums.append(int(s))
    for i in range(1,len(nums)):
        later = nums[i]
        for j in range(i-1,-1,-1):
            earlier = nums[j]
            if later in order and earlier in order[later]:
                valid = False
                break
        if not valid:
            break
    if valid:
        ans += nums[len(nums)//2]
print(ans)