def initNext(p):
    M = len(p)
    next[0] = -1
    i=1
    j=0
    while(i<M):
        next[i] = j
        while((j>=0) and (p[i] != p[j])):
            j=next[j]
        i=i+1
        j=j+1

patterns = [
    "aaaaaaaaa",
    "00000001",
    "10100111",
    "ababca",
    "abababca",
    "abcabcabc",
    "abcabcacab",
    "abracadabra"
]
for pattern in patterns:
    next = [0] * (len(pattern))
    initNext(pattern)
    print(f"Pattern: {pattern}, Next: {next}")