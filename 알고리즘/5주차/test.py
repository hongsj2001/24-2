import random, time
from sort import *
import matplotlib.pyplot as plt

#랜덤 리스트 생성
N = 5000
n = 5

nList=[]
sortList1 = []
sortList2 = []
timeList1 = []
timeList2 = []

for i in range(n):
    nList.append((i+1)*N)
    sortList1.append([-1])	# 더미 키
    for j in range((i+1)*N):
        sortList1[i].append(random.randint(1, N))
    print(sortList1[i][i*N-1])

for i in range(n):
    nList.append((i+1)*N)
    sortList2.append([-1])	# 더미 키
    for j in range((i+1)*N):
        sortList2[i].append(random.randint(1, N))
    print(sortList2[i][i*N-1])


#시간 측정
for i in range(n):
    start_time = time.time()
    x=bubbleSort(sortList1[i], len(sortList1[i])-1)
    end_time = time.time() - start_time
    timeList1.append(end_time)
    checkSort(x, N)
    print('버블 정렬의 실행 시간 (정렬) (N = %d) : %0.3f'%(nList[i], end_time))

    start_time = time.time()
    x=cocktailShakerSort(sortList2[i], len(sortList2[i])-1)
    end_time = time.time() - start_time
    timeList1.append(end_time)
    checkSort(x, N)
    print('칵테일 쉐이커 정렬의 실행 시간 (정렬) (N = %d) : %0.3f'%(nList[i], end_time))



plt.title('bubbleSort (sort)')
plt.xlabel("N")
plt.ylabel("time (s)")
for i in range(len(nList)):
    height = timeList1[i]
    plt.text(nList[i], height + 0.001, '%.3f' %height, ha='center', va='bottom', size = 12)
plt.plot(nList, timeList1, marker="o",label="bubbleSorttime")
plt.plot(nList, timeList2, marker="x",label="cocktailtime")
plt.legend()
plt.show()