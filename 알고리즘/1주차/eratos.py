def eratos(a, n):
    a[1] = 0
    i=2
    while (i<n/2):
        j=2
        while(i*j<=n):
            a[i*j]=0
            j=j+1
        i=i+1
    return a

N = int(input('N = '))
while N < 1:
    print(N, '은(는) 자연수가 아닙니다.')
    N = int(input('N = '))
A = list(range(N+1))
res = eratos(A, N)
for i in range(N+1):
    if res[i]: print(i, end=' ')