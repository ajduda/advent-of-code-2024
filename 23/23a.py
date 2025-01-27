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

lanParties = set()

for k in connections:
    if k[0] == 't':
        for connection1 in connections[k]:
            likeConnections = connections[k] & connections[connection1]
            for connection2 in likeConnections:
                l = [k,connection1,connection2]
                l.sort()
                lanParties.add((l[0],l[1],l[2]))



print(len(lanParties))