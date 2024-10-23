import numpy as np
import matplotlib.pyplot as plt

# x 범위
x = np.linspace(-2, 2, 1000)
# 함수 정의
y = np.sin(10 * x) - x

# 그래프 그리기
plt.plot(x, y)
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Graph of f(x) = sin(10x) - x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

#x=-1과 1사이에 존재 확인

