import random, time
from sort import *
import matplotlib.pyplot as plt

N = 35000
a = [-1]	# 더미 키
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time
print('선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)