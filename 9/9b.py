file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

ans = 0

hardDrive = []
block = 0
writing = True
gaps = []

for line in z.split('\n'):
    for c in line:
        if writing:
            for i in range(int(c)):
                hardDrive.append(block)
        else:
            gaps.append((len(hardDrive),int(c)))
            for i in range(int(c)):
                hardDrive.append(-1)
        writing = not writing
        if writing:
            block += 1

lptr = 0
rptr = len(hardDrive)-1

movedBlocks = set()

# lots of debugging today
while rptr >= 0:
    #print(f'GAPS: {gaps}')
    #print(f'HARDDRIVE: {hardDrive}')
    #print(f'RPTR: {rptr}')
    while hardDrive[rptr] == -1:
        rptr -= 1
    num = hardDrive[rptr]
    rbound = rptr
    while hardDrive[rptr-1] == num:
        rptr -= 1
    length = rbound - rptr + 1
    if num in movedBlocks:
        rptr -= 1
        #print(f'ENCOUNTERED {num} again, skipping! rptr is now at {rptr}')
        continue
    movedBlocks.add(num)
    #print(f'SEARCHING WHERE TO PLACE {num} block')
    #print(f'{num} BLOCK HAS LENGTH {length}')
    gapIdx = 0
    while gapIdx < len(gaps) and gaps[gapIdx][1] < length:
        gapIdx += 1
    if gapIdx == len(gaps) or gaps[gapIdx][0] > rptr:
        continue  # could not move this file back at all
    #print(f'PUTTING BLOCK {num} at {gaps[gapIdx]}')
    for i in range(gaps[gapIdx][0],gaps[gapIdx][0]+length):
        hardDrive[i] = num
    if gaps[gapIdx][1] > length:
        gaps[gapIdx] = (gaps[gapIdx][0]+length,gaps[gapIdx][1]-length)
    else:
        gaps.pop(gapIdx)
    for i in range(rptr,rbound+1):
        hardDrive[i] = -1
    

#print(hardDrive)

for i in range(len(hardDrive)):
    if hardDrive[i] != -1:
        ans += i*hardDrive[i]
    
print(ans)