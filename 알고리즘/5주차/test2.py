import random, time
from sort import *
import matplotlib.pyplot as plt

N = 10000
a = [-1]
b = [-1]	# 더미 키
for i in range(N):
    number = random.randint(1, N)
    a.append(number)
    b.append(number)
acpy = a.copy()
start_time = time.time()
mergeSort(a,acpy,1, N)
end_time = time.time() - start_time
print('합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))

start_time = time.time()
naturalMerge(b, N)
end_time = time.time() - start_time
print('자연 합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
