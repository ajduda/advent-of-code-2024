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
    
    maxLen = 2**(len(nums)-1)
    for i in range(maxLen):
        value = nums[0]
        bit = 1
        #print(f'trying i={i}')
        #print(value)
        for j in range(1,len(nums)):
            nextVal = nums[j]
            if i & bit >= 1:
                #print('+')
                value += nextVal
            else:
                #print('*')
                value *= nextVal
            #print(nextVal)
            #print('=')
            bit <<= 1
            #print(value)

        if value == total:
            ans += total
            break
        

print(ans)