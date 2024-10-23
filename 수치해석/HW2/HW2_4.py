import math

# 고정점 반복법
def g(x):
    return math.cos(x)  # f(x)=cos(x)-x에 대해 g(x)=cos(x) 정의

def fixed_point_iteration(x0, kmax=40, tol=1e-4):
    for k in range(kmax):
        y = g(x0)
        if abs(y - x0) < tol:
            break
        x0 = y
        print(x0)
    return x0

# 초기값 설정
x0 = 0
result = fixed_point_iteration(x0)

print("근사해:", result)