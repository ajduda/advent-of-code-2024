file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

for line in z.split('\n'):
    l,r = line.split(": ")
    total = int(l)
    nums = []
    for n in r.split(' '):
        nums.append(int(n))
    
    maxLen = 3**(len(nums)-1)
    for i in range(maxLen):
        operation = i
        value = nums[0]
        for j in range(1,len(nums)):
            nextVal = nums[j]
            if operation % 3 == 0:
                value += nextVal
            elif operation % 3 == 1:
                value *= nextVal
            else:
                value = int(str(value)+str(nextVal))
            operation //= 3

        if value == total:
            ans += total
            break
        

print(ans)