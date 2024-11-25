import random, time
import matplotlib.pyplot as plt
from sort import *
import sys
sys.setrecursionlimit(10**9)


#랜덤 리스트 생성
N = 5000
n = 10

nList=[]
sortList = []
timeList = []
copyList = []


#랜덤
for i in range(n):
    nList.append((i+1)*N)
    sortList.append([-1])#더미 키
    for j in range((i+1)*N):
        sortList[i].append(random.randint(1, (i+1)*N))
    copyList.append(sortList[i].copy())
print(nList)
'''

#역방향
for i in range(n):
    nList.append((i+1)*N)
    sortList.append([-1])#더미 키
    for j in range((i+1)*N,0,-1):
        sortList[i].append(j)
    copyList.append(sortList[i].copy())
print(nList)


#순방향
for i in range(n):
    nList.append((i+1)*N)
    sortList.append([-1])#더미 키
    for j in range((i+1)*N):
        sortList[i].append(j)
    copyList.append(sortList[i].copy())
print(nList)
'''
#시간 측정
for i in range(n):
    start_time = time.time()
    heapSort(sortList[i], (len(sortList[i])-1))
    end_time = time.time() - start_time
    timeList.append(end_time)
    checkSort(sortList[i], N)
    print('힙 정렬의 실행 시간 (랜덤) (N = %d) : %0.3f'%(nList[i], end_time))



plt.title('HeapSort (Random)')
plt.xlabel("N")
plt.ylabel("time (s)")
for i in range(len(nList)):
    height = timeList[i]
    plt.text(nList[i], height + 0.001, '%.3f' %height, ha='center', va='bottom', size = 12)
plt.plot(nList, timeList, marker="o",label="time")
plt.legend()
plt.show()