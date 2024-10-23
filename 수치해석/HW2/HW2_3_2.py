import math

# 함수 정의
def f(x):
    return math.sin(x)-x

# 이분법 함수 정의
def bisection(a, b, tol):
    while b - a > tol:  # 구간의 절반 크기가 tolerance보다 클 때 반복
        c = a+(b-a)/2  # 중간점
        if f(a) * f(c) < 0:  # a와 c 사이에 근이 있는 경우
            b = c
        else:  # c와 b 사이에 근이 있는 경우
            a = c

    return c

# 초기 구간 [a, b] 및 tolerance 설정
a = -1
b = 1
tolerance = 1e-5

# 이분법 실행
root = bisection(a, b, tolerance)

# 결과 출력
if root is not None:
    print(f"근의 근사값은: {root}")
