file = 'test.txt'
file = 'input.txt'


memoize = {}

def findPossible(pattern,colors,maxLen):
    if pattern in memoize:
        return memoize[pattern]
    c = pattern[0] # letter to look for
    if pattern in colors[c]:
        memoize[pattern] = True
        return True
    for i in range(1,maxLen+1):
        if pattern[:i] in colors[c]:
            if findPossible(pattern[i:],colors,maxLen):
                memoize[pattern] = True
                return True
    
    memoize[pattern] = False
    return False




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
i = 0
for line in sections[1].split('\n'):
    print(i)
    if findPossible(line,colors,maxLen):
        ans += 1
    i += 1

print(ans)