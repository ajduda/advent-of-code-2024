file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

newInput = ""
validChunks = z.split("do()")
for chunk in validChunks:
    subChunks = chunk.split("don't()")
    newInput += subChunks[0]

chunks = newInput.split('mul(')
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

print(ans)