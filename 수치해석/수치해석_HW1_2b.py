import math
import matplotlib.pyplot as plt

#cos(x) 매클로린 급수 사용자 정의 함수
def mac (x,n):
  f=0
  for i in range (n):
    if(i%2 == 1):
        f-=(x**(i*2))/math.factorial(i*2)
    else:
       f+=(x**(i*2))/math.factorial(i*2)
  return f


x = []
y = []
#항 수를 0~ 20까지 증가
for i in range(20):
   x.append(i)

real = math.cos(math.pi/3) #실제 값

#각 항수에 대한 상대오차 계산
for i in x:
    approx = mac(math.pi/3,i) #근사값
    ocha = abs((real - approx) / real) #상대오차
    y.append(ocha)


#그래프 생성
plt.title("Relative Error")
plt.xlabel("term")
plt.ylabel("Relative Error")
plt.plot(x, y,label="Relative Error")
plt.semilogy(base=10) #밑이 10인 로그 스케일로 변경
plt.show()


print("참값 : {}".format(real))
print("근사값 : {}".format(approx))
print("상대오차 : {}".format(ocha))