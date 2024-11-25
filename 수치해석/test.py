import numpy as np

# 변수 정의
n = 3
A = np.array([[64, 64, 4], [2, 2, 2], [3, -1, 0]], dtype=float)
b = np.array([17, 0, 0], dtype=float)

# Forward elimination (전방 소거)
for j in range(n-1):
    # 부분 피벗팅
    abs_column = np.abs(A[j:n, j])  # 열의 절대값 추출
    big, l = np.max(abs_column), np.argmax(abs_column) + j

    # A의 j번째 행과 l번째 행 교환
    A[[j, l], :] = A[[l, j], :]

    # b 벡터의 j번째 값과 l번째 값 교환
    b[j], b[l] = b[l], b[j]

    # 행에 대한 소거 작업 수행
    for i in range(j+1, n):
        factor = A[i, j] / A[j, j]
        A[i, :] = A[i, :] - factor * A[j, :]
        b[i] = b[i] - factor * b[j]

# Backward substitution (역진대입법)
x = np.zeros(n)  # 해를 저장할 벡터 x 초기화

# n번째 변수 계산
x[n-1] = b[n-1] / A[n-1, n-1]

# 나머지 변수 계산 (역순으로 계산)
for i in range(n-2, -1, -1):
    s = 0
    for k in range(i+1, n):
        s += A[i, k] * x[k]
    x[i] = (b[i] - s) / A[i, i]

# 결과 출력
print("해 벡터 x:")
print(x)
