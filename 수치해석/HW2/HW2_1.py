import numpy as np
import math
from scipy.linalg import lu, solve_triangular

A = np.array([[8,20,15],[20,80,50],[15,50,60]], dtype= float)
b = np.array([50,250,100], dtype= float)
print(np.linalg.eig(A)) #행렬 A의 고유치 > 0 


# 3X3 Cholesky 분해
def cholesky3(A, transpose = True):
    L11 = math.sqrt((A[0][0])) 
    L21 = A[1][0] / L11
    L22 = math.sqrt((A[1][1]-L21**2))
    L31 = A[2][0] / L11
    L32 = (A[2][1] - L31*L21) / L22
    L33 = math.sqrt(A[2][2] - L31**2 - L32**2)
    L = np.array([[L11,0,0],[L21,L22,0],[L31,L32,L33]])


    if(transpose):
        return np.transpose(L)
    else:
        return L

# Backward substitution (역진대입법)
def backwardSubtitution(A,b,n):
    x = np.zeros(n)  # 해를 저장할 벡터 x 초기화

    # n번째 변수 계산
    x[n-1] = b[n-1] / A[n-1, n-1]

    # 나머지 변수 계산 (역순으로 계산)
    for i in range(n-2, -1, -1):
        s = 0
        for k in range(i+1, n):
            s += A[i, k] * x[k]
        x[i] = (b[i] - s) / A[i, i]

    return x


# Forward substitution (전진대입법)
def forwardSubtitution(A,b,n):
    x = np.zeros(n)  # 해를 저장할 벡터 x 초기화

    # n번째 변수 계산
    x[0] = b[0] / A[0, 0]

    # 나머지 변수 계산 (역순으로 계산)
    for i in range(1, n):
        s = 0
        for k in range(i+1, n):
            s += A[i, k] * x[k]
        x[i] = (b[i] - s) / A[i, i]

    return x


print("L^T = ",cholesky3(A,True))
print("L = ",cholesky3(A,False))


# 1단계: Ly = b를 풀어 y를 구합니다. (전방 대입)
y = solve_triangular(al, b, lower=True)
print("전방 대입 결과 y:\n", y)

# 2단계: L^T x = y를 풀어 x를 구합니다. (후방 대입)
x = solve_triangular(L.T, y, lower=False)
print("선형 시스템의 해 x:\n", x)

