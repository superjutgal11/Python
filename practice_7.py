# 7강 _ 숫자 처리 함수

# 절댓값 함수 , abs(a)
print(abs(-3.5))

# power 함수 = 거듭제곱 함수 , pow(a,b) = a ** b
print(pow(4,3)) # 4의 3승의 값

# max 함수 = 입력받은 수 중 가장 큰 값 출력. max(x1,x2,x3, ...)
print(max(10,22,-3,4.4,12,53)) # 가장 큰 수인 53 출력

# 1의 자리에서 반올림 함수 , round(a)
print(round(3.49)) # 3.5미만이기에 3으로 반올림
print(round(-4.99)) # -4.5 이하이기에 -5 출력

# 파이썬에서 제공하는 math 라이브러리를 이용하는 방법
# from math import * 를 쓰면 math 라이브러리 안의 모든 기능을 쓰겠다는 의미
from math import *
print(floor(4.99)) #math 라이브러리의 내림함수 floor(a)
print(ceil(4.01)) #math 라이브러리의 올림함수 ceil(a)
print(sqrt(4)) # math 라이브러리의 제곱근 함수 sqrt(a)