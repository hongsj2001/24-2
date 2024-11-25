import math

#cos(x) 매클로린 급수 사용자 정의 함수
def mac (x,n):
  f=0
  for i in range (n):
    if(i%2 == 1):
        f-=(x**(i*2))/math.factorial(i*2)
    else:
       f+=(x**(i*2))/math.factorial(i*2)
  return f

real = math.cos(math.pi/3) #실제 값
approx = mac(math.pi/3,4) #근사값
ocha = abs((real - approx) / real) #상대오차

print("참값 : {}".format(real))
print("근사값 : {}".format(approx))
print("상대오차 : {}".format(ocha))