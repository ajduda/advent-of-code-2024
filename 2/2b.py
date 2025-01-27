file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    nums = []
    l = line.split()
    for n in l:
        nums.append(int(n))
    direction = set()
    safe = True
    for i in range(1,len(nums)):
        r = nums[i]
        l = nums[i-1]
        if abs(l-r) > 3 or abs(l-r) == 0:
            safe = False
            break
        if l > r:
            direction.add('+')
            if '-' in direction:
                safe = False
                break
        else:
            direction.add('-')
            if '+' in direction:
                safe = False
                break

    if safe:
        ans += 1
    else:
        oldNums = nums.copy()
        for j in range(len(oldNums)):
            nums.pop(j)
            safe = True
            direction = set()
            for i in range(1,len(nums)):
                r = nums[i]
                l = nums[i-1]
                if abs(l-r) > 3 or abs(l-r) == 0:
                    safe = False
                    break
                if l > r:
                    direction.add('+')
                    if '-' in direction:
                        safe = False
                        break
                else:
                    direction.add('-')
                    if '+' in direction:
                        safe = False
                        break
            if safe:
                ans += 1
                break

print(ans)