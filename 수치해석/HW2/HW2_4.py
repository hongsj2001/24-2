import math
import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def f(x):
    return (1 / math.cos(x)) - (x**2 - 1) / 2*x

# 이분법 함수 정의
def bisection(a, b, tol):
    l = []
    while b - a > tol:  # 구간의 절반 크기가 tolerance보다 클 때 반복
        c = a+(b-a)/2  # 중간점
        if f(a) * f(c) < 0:  # a와 c 사이에 근이 있는 경우
            b = c
        else:  # c와 b 사이에 근이 있는 경우
            a = c
        l.append(c)

    return l,c

# 초기 구간 [a, b] 및 tolerance 설정
a = 0
b = 2
tolerance = 1e-10

# 이분법 실행
l,c = bisection(a, b, tolerance)
print("근의 근사값은 : ", c)
x = np.arange(1,len(l)+1,1)
plt.plot(x, l)
plt.title('')
plt.xlabel('iter')
plt.ylabel('numerical')
plt.grid(True)
plt.show()

