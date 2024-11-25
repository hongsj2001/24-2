import random, time
import matplotlib.pyplot as plt
from sort import *
import sys
sys.setrecursionlimit(100000000)




N = 5000
a = [-1]	# 더미 키
'''
for i in range(N):
    a.append(random.randint(1, N))
'''
for i in range(N):
    a.append(i)
b = a.copy()
start_time = time.time()
mergeSort(a,b,1,N)
end_time = time.time() - start_time
print('합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)