def longestSequenceList(a, s, n):
    max_len=1
    i=0
    longest=[]
    while(i<n):
        now=[]
        left=a[i]-1
        right=a[i]+1
        count=1
        now.append(a[i])
        while(left in s):
            count=count+1
            now.append(left)
            s.remove(left)
            left=left-1
        while(right in s):
            count=count+1
            now.append(right)
            s.remove(right)
            right=right+1
        max_len=max(max_len,count)
        if(len(longest)<=len(now)):
            longest = now
        i=i+1
    longest.sort()
    return max_len,longest


import random
N = int(input('난수의 개수 : '))
while N < 1:
    print('난수의 개수는 자연수여야 합니다.')
    N = int(input('난수의 개수 : '))
A = []
for i in range(N):
    A.append(random.randint(1, N))
print('리스트 : ', A)
S = set(A)
print('집합 : ', S)        
len_longest, longest_list = longestSequenceList(A, S, N)
print('최장 연속 순차의 길이 : ', len_longest)
print('최장 연속 순차 : ', longest_list)