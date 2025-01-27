file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

connections = {}

for line in z.split('\n'):
    l,r = line.split('-')
    if l not in connections:
        connections[l] = set()
    if r not in connections:
        connections[r] = set()
    connections[l].add(r)
    connections[r].add(l)
    #add self connections so set intersections will just work
    connections[l].add(l)
    connections[r].add(r)

biggestGroup = 0
for k1 in connections:
    groupTosubset = list(connections[k1])
    permutations = 2**len(groupTosubset)
    for i in range(permutations):
        sharedGroup = set()
        for j in range(len(groupTosubset)):
            if (2**j) & i > 0:
                sharedGroup.add(groupTosubset[j])
        size = len(sharedGroup)
        if size > biggestGroup:  # only check if this can be bigger
            valid = True
            for cpu in sharedGroup:
                if len(sharedGroup & connections[cpu]) != size:
                    valid = False
                    break
            if valid:
                biggestGroupStr = ""
                biggestGroup = size
                l = list(sharedGroup)
                l.sort()
                for host in l:
                    biggestGroupStr += host
                    biggestGroupStr += ','
                biggestGroupStr = biggestGroupStr[:-1]

print(biggestGroupStr)