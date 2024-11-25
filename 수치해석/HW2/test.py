import numpy as np
import matplotlib.pyplot as plt

# 함수 f(x) 정의: f(x) = tan(x) * tanh(x) + 1
def f(x):
    return np.tan(x) * np.tanh(x) + 1

# 유한 차분 근사화 함수 정의
def finite_difference_derivative(f, x, h=1e-4):
    return (f(x + h) - f(x)) / h
# Newton 방법 함수
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    errors = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(f, x)
        xold = x
        x = x - fx / dfx
        error = abs(x - xold)
        errors.append(error)
        if error < tol:
            break
    return x, errors
# 초기값과 Newton 방법 실행
x0 = 1.0
approx_root, errors = newton_method(f, finite_difference_derivative, x0)

# 결과 출력
print("근사 해:", approx_root)
# 수렴 속도 그래프
plt.subplot(131,1)
plt.semilogy(errors, label="Error")
plt.xlabel("Iteration")
plt.ylabel("Error (log scale)")
plt.title("Newton Method Convergence for tan(x)*tanh(x) = -1")
plt.legend()
plt.show()
