def index(c):
    if ord(c) == 32: return 0
    else: return ord(c)-64

def RKfirst(p, t, k):
    dM=1
    h1=0
    h2=0
    M = len(p)
    N = len(t)
    i=1
    while(i<M):
        dM = (d*dM)%q
        i+=1
    i=0
    while(i<M):
        h1 = (h1*d + index(p[i]))%q
        h2 = (h2*d + index(t[i]))%q
        i+=1
    i=0
    while(h1!=h2):
        if(i+M>=N):
            return N
        h2 = (h2 + d*q - index(t[i])*dM) % q
        h2 = (h2*d + index(t[i+M])) % q
        if(i>N-M):
            return N
        i+=1
    return i

def RK(p, t, k):
    dM=1
    h1=0
    h2=0
    M = len(p)
    N = len(t)
    i=1
    while(i<M):
        dM = (d*dM)%q
        i+=1
    i=0
    while(i<M):
        h1 = (h1*d + index(p[i]))%q
        i+=1
    i=k
    j=0
    while(i<N and j<M):
        h2 = (h2*d + index(t[i]))%q
        i+=1
        j+=1
    i=k
    while(h1!=h2):
        if(i+M>=N):
            return N
        h2 = (h2 + d*q - index(t[i])*dM) % q
        h2 = (h2*d + index(t[i+M])) % q
        if(i>N-M):
            return N
        i+=1
    return i

q = 33554393
d = 32
text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION' + '\0'
pattern = 'ATION'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = RK(pattern, text, K)
    K = pos + 1
    if K <= N - M: print('패턴이 나타난 위치 : ', pos)
    else: break
print('스트링 탐색 종료')