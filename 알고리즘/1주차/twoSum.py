def twoSum(a, n, t):
    i=0
    while(i<n):
        j=i+1
        while(j<n):
            if((a[i]+a[j])==t):
                print("{}번째와 {}번째의 원소 ".format(i+1,j+1))
            j=j+1
        i=i+1

import random
N = int(input('리스트의 원소 개수 : '))
A = []
for i in range(N):
    A.append(random.randint(1, N*2))
print('리스트 : ', A)    
T = int(input('목표값 입력 : '))
print('두 수의 합이 %d인 원소 쌍'%T)
twoSum(A, N, T)