import math
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# x 범위
x = np.linspace(-2, 2, 1000)
# 함수 정의
y = (1.0 / np.tan(x)-((x**2)-1)/2*x)
z=x
# 그래프 그리기
plt.plot(x, y,x,z)
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Graph of f(x) = sin(10x) - x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# 고정점 반복법
def g(x):
    return ((x*x)-1)/2*(1.0 / math.tan(x))  # f(x)=cot(x) - (x^2-1)/2x 에 대해 g(x) = (x^2-1)/2cot(x) 정의

def fixed_point_iteration(x0, kmax=40, tol=1e-10):
    for k in range(kmax):
        y = g(x0)
        if abs(y - x0) < tol:
            break
        x0 = y
        print(x0)
    return x0

# 초기값 설정
x0 = 0.3
result = fixed_point_iteration(x0)