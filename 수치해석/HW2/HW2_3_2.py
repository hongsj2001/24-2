import math
import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def f(x):
    return math.sin(10*x)-x

# 이분법 함수 정의
def bisection(a, b, tol):
    clist = []
    while b - a > tol:  # 구간의 절반 크기가 tolerance보다 클 때 반복
        c = a+(b-a)/2  # 중간점
        if f(a) * f(c) < 0:  # a와 c 사이에 근이 있는 경우
            b = c
        else:  # c와 b 사이에 근이 있는 경우
            a = c
        clist.append(c)

    return clist, c

# 대략적 해의 위치 구간 및 tolerance 설정
xlist= [[-1,-0.75],[-0.75,-0.5],[-0.5,-0.2],[-0.2,0.1],[0.1,0.5],[0.5,0.72],[0.72,1]]
tolerance = 1e-10
alist=[]
iterlist = []
for i in (xlist):
    iter,q = bisection(i[0],i[1],tolerance)
    alist.append(q)
    iterlist.append(iter)

# 이분법 실행


# 결과 출력
if alist is not None:
    print(f"근의 근사값은: {alist}")

print(len(iterlist[0]))
plt.subplot(241)
plt.plot(np.arange(1,len(iterlist[0])+1,1), iterlist[0])
plt.xlabel('iter')
plt.grid(True)

plt.subplot(242)
plt.plot(np.arange(1,len(iterlist[1])+1,1), iterlist[1])
plt.xlabel('iter')
plt.grid(True)

plt.subplot(243)
plt.plot(np.arange(1,len(iterlist[2])+1,1), iterlist[2])
plt.xlabel('iter')
plt.grid(True)

plt.subplot(244)
plt.plot(np.arange(1,len(iterlist[3])+1,1), iterlist[3])
plt.xlabel('iter')
plt.grid(True)

plt.subplot(245)
plt.plot(np.arange(1,len(iterlist[4])+1,1), iterlist[4])
plt.xlabel('iter')
plt.grid(True)

plt.subplot(246)
plt.plot(np.arange(1,len(iterlist[5])+1,1), iterlist[5])
plt.xlabel('iter')
plt.grid(True)

plt.subplot(247)
plt.plot(np.arange(1,len(iterlist[6])+1,1), iterlist[6])
plt.xlabel('iter')
plt.grid(True)
plt.show()
