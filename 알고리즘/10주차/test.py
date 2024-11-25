def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c) - 64

def initSkip(p):
    M = len(p)
    for i in range(NUM):
        skip[i] = M
    for i in range(M - 1):
        skip[index(p[i])] = M - i - 1

def BM(p, t, k):
    M = len(p)
    N = len(t)
    initSkip(p)
    i = k + M - 1
    j = M - 1
    
    while j >= 0:
        if (i >= N - 1):
                return N
        while t[i] != p[j]:
            if (i >= N - 1):
                return N
            s = skip[index(t[i])]
            if (M - j > s):
                i = i + M - j
            else:
                i = i + s
            j = M - 1
            if (i >= N):
                return N
        i -= 1
        j -= 1

    return i + 1



# 상수 및 초기화
NUM = 26
skip = [0] * NUM
text = 'STRING STARTING CONSISTING'
pattern = 'ING'
M = len(pattern)
N = len(text)
K = 0
# 패턴 검색 루프
while True:
    pos = BM(pattern, text, K)
    if pos >= N - 1:  # N-1을 넘으면 탐색 종료
        break
    print('패턴이 나타난 위치 :', pos)
    K = pos + 1  # 다음 위치부터 다시 탐색

print('스트링 탐색 종료')
