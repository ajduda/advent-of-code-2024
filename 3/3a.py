file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

chunks = z.split('mul(')
for chunk in chunks[1:]:
    i = chunk.find(')')
    if i == -1:
        continue
    nums = chunk[:i].split(',')
    if len(nums) != 2:
        print('FAILURE')
        print(nums)
        continue
    
    if nums[0].isdecimal() and nums[1].isdecimal() and len(nums[0]) < 4 and len(nums[1]) < 4:
        #print('SUCCESS')
        #print(nums)
        ans += (int(nums[0])*int(nums[1]))
    else:
        pass
        #print('FAILURE')
        #print(nums)

print(ans)