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

def KMP(p, t, k):
    M = len(p)
    N = len(t)
    initNext(p)
    i=k
    j=0
    while((i<N) and (j<M)):
        while((j>=0) and (t[i] != p[j])):
            j =next[j]
        i=i+1
        j=j+1
    if(j==M):
        return i-M
    else:
        return i

next = [0] * 50
text = 'ababababcababababcaabbabababca' + '\0'
pattern = 'abababca'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = KMP(pattern, text, K)
    K = pos + 1
    if K <= N - M: print('패턴이 나타난 위치 : ', pos)
    else: break
print('스트링 탐색 종료')