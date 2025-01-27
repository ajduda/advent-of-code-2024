file = 'test.txt'
file = 'input.txt'


memoize = {}

def findPossible(pattern,colors,maxLen):
    if pattern in memoize:
        return memoize[pattern]
    
    if len(pattern) == 0:
        return 0
    
    c = pattern[0] # letter to look for
    


    ret = 0

    if pattern in colors[c]:
        ret = 1
    
    for i in range(1,maxLen+1):
        if pattern[:i] in colors[c]:
            ret += findPossible(pattern[i:],colors,maxLen)
                
    
    memoize[pattern] = ret
    return ret




with open(file) as inp:
    z = inp.read()
    z = z.strip()


sections = z.split('\n\n')
colors = {}  # colors sorted by start letter
for i in range(97,97+26):
    colors[chr(i)] = set()

maxLen = -1

for color in sections[0].split(', '):
    startChar = color[0]
    colors[startChar].add(color)
    if len(color) > maxLen:
        maxLen = len(color)

ans = 0
for line in sections[1].split('\n'):
    ans += findPossible(line,colors,maxLen)
print(ans)