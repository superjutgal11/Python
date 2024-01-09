# 8강 _ 랜덤 함수

# 랜덤(=난수) 라이브러리를 사용하겠다고 선언한다.
from random import *

# random() 함수는 0.0 에서  1.0 미만의 실수형 랜덤값을 생성
print(random()) # 2개 print 전부 각자 다른 값이 출력된다.
print(float(random())) # 디폴트는 float 형이다.
# 0.5398007035182966   0.3983650362507303 처럼 값이 나옴

# random()*10 함수는 0.0 에서 10.0 미만의 실수형 랜덤값을 생성
print(random()*10)
print(random()*10)
# 9.887161008247862   7.63564981374278 처럼 값이 나옴

# 만약 0부터 X-1 까지의 정수값만을 받고 싶다면 int(random() * X )  
# 만약 0부터 X 까지의 정수값만을 받고 싶다면 int(random() * (X+1) ) 
print(int(random()*10)) # 이렇게 하면 0에서 9이하 정수형 난수 출력
print(int(random()*11)) # 로 하면 0이상 10이하의 정수형 난수 출력
print(int(random()*10+1)) 
#위처럼 하면 1이상 10이하의 정수형 난수 출력이므로 주의할 것. (X-1)해서 수 넣기.

# 만약 Y이상 X미만의 랜덤 실수형 난수를 출력하고 싶다면
# float(random()*(X-Y))+Y )
print((random()*9)+1) # 1 이상 10 미만의 실수형 난수
print((random()*3)+2) # 2 이상 5 미만의 실수형 난수
print((random()*50)+50) # 50 이상 100 미만의 실수형 난수

# 만약 Y 이상 X 이하의 랜덤 정수형 난수를 출력하고 싶다면
# int(random()*(X-Y+1))+Y)
print(int(random()*10)+2) # 2 이상 10이하의 정수형 난수 
print(int(random()*5)+3) # 3 이상 7이하의 정수형 난수
print(int(random()*6)-10) # -10 이상 -5 미만의 정수형 난수

# 정수형 난수의 범위를 더 단순하게 설정하는 방법으로 randrange(Y,X) 가 있음.
# randrange(Y,X) 는 Y 이상 X 미만의 정수형값이 랜덤으로 생성됨.
print(randrange(1,5)) #  1 이상 5 미만 정수형 난수
print(randrange(100,121)) # 100 ~ 120 의 정수형 난수

# randint(Y,X) 는 Y 이상 X 이하의 정수형 난수를 생성한다. 
# 양 끝의 정수를 포함하는 범위의 난수를 생성하는 함수.
print(randint(1,5)) # 1 이상 5 이하의 정수형 난수