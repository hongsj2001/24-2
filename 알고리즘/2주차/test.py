import random, time
from sort import *
import matplotlib.pyplot as plt

#랜덤 리스트 생성
N = 5000
n = 10

nList=[]
sortList = []
timeList = []

for i in range(n):
    nList.append((i+1)*N)
    sortList.append([-1])	# 더미 키
    for j in range((i+1)*N):
        sortList[i].append(j)
    print(sortList[i][i*N-1])
#시간 측정
for i in range(n):
    start_time = time.time()
    x=bubbleSort(sortList[i], len(sortList[i])-1)
    end_time = time.time() - start_time
    timeList.append(end_time)
    checkSort(x, N)
    print('버블 정렬의 실행 시간 (정렬) (N = %d) : %0.3f'%(nList[i], end_time))



plt.title('bubbleSort (sort)')
plt.xlabel("N")
plt.ylabel("time (s)")
for i in range(len(nList)):
    height = timeList[i]
    plt.text(nList[i], height + 0.001, '%.3f' %height, ha='center', va='bottom', size = 12)
plt.plot(nList, timeList, marker="o",label="time")
plt.legend()
plt.show()

