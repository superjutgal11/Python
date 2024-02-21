'''
메소드 : 특정 용도의 코드를 묶어 놓은 것으로, 처음 한번 작성으로 나중에 필요 시마다 계속 불러 쓸 수 있다.
함수를 정의하기 전에 함수를 호출할 수 없고 빈 함수를 만들 땐 코드 부분에 pass 를 넣는다.
pass는 아무 일을 하지 않아도 함수의 틀을 유지하려 할 때 사용한다.

매개변수 : 함수의 괄호 안에 넣는 변수
인수 : 함수 호출 시 안에 넣는 변수

함수 독스트링 : 함수의 콜론 다음줄에 """ 내용 """ 처럼 문자열을 입력하면 해당 함수의 설명을 넣을 수 있다.
독스트링의 위에 코드가 올 수 없으며 독스트링을 출력하려면 함수이름.__doc__ 를 쓴다.
'''


# 함수 정의,호출 연습
def 함수_1():
    print("연습중입니다.")

함수_1()

'''
# 함수 매개변수,인수 널기 연습
def 함수_2(매개변수1,매개변수2): # 함수 괄호에 넣는 변수
    매개변수1=int(매개변수1)
    매개변수2=int(매개변수2)
    매개변수_합=매개변수1+매개변수2 # 정수형으로 바꿔 값을 더함
    print("두 정수의 합은"+str(매개변수_합)) # str형으로 바꿔서 print

인수1,인수2=input("두 정수를 ,로 구분하여 2개를 입력하세요 : ").split(',')
함수_2(인수1,인수2) # 함수 호출 때 넣는 변수를 인수라 함
두 정수를 ,로 구분하여 2개를 입력하세요 : 10,20
두 정수의 합은30'''


# 함수 독스트링

def 함수_3(a,b):
    """
a 는 학생의 이름이고, b는 학생의 나이입니다.
    """
    print(a,b)

c="정재형"
d=25
함수_3(c,d)
print(함수_3.__doc__)

'''정재형 25
a 는 학생의 이름이고, b는 학생의 나이입니다.'''


'''
리턴 : 함수에서 값을 함수 바깥으로 반환할 때 return을 사용한다.
return에 값을 미지정한 경우 None(다른언어에서 NULL에 해당)을 리턴한다.
반환값은 함수 외부에서 변수로 쓰거나 다른 함수에 값을 넣어줄 수 있다.

매개변수없이 반환값만 있는 함수의 경우엔 return에 반환치를 바로 써주면 된다.

return과 if문 등을 사용하여 함수 중간에 빠져나오게 할 수 있다.
'''

def 함수_4():
    return 1 # 값 1을 그냥 반환

def 함수_5():
    return "안녕" # "안녕"을 그냥 반환.

a1=함수_4() # 변수에 넣을 수도 있고
print(a1)
print(함수_5()) # 함수에 직접 넣을수도 있다.

def 함수_6(a,b):
    return a+b

c = 10
d = 20
print(함수_6(c,d)) # 이런 식으로도 가능


# return으로 함수 중간에 바져나오기도 가능

def 함수_7(a):
    if a < 0: # a가 음수일 때
        print("a는 음수") # 이 조건 맞으면 바로 코드실행 후 탈출
    elif a==0: 
        print("a는 0") # 이 조건 맞으면 바로 코드실행 후 탈출
    print('a는 양수') # 위 조건 둘 다 아니면(양수이면) 이거 실행

a = 0
함수_7(a)

'''
함수에서 값 여러개를 반환할 땐 return 반환값1,반환값2처럼 콤마로 구분하여 지정해야 한다.
'''

# def 함수_8(a,b,c):
#     """a와 b는 연산될 값이고 c는 연산자임."""
#     if c=='+':
#         return "둘의 합은",a+b
#     if c=='-':
#         return "둘의 차는",a-b
#     else:
#         return "연산자는 ","+외 -만 지원함"
    
# z1,z2,z3=input("두 숫자와 연산자(+,-)를 ,로 구분하여 입력 > ").split(",")
# z1=int(z1)
# z2=int(z2)
# x1,x2=함수_8(z1,z2,z3)
# print("{0}{1}".format(x1,x2))

'''
결과 : 
두 숫자와 연산자(+,-)를 ,로 구분하여 입력 > 10,20,+
둘의 합은30

두 숫자와 연산자(+,-)를 ,로 구분하여 입력 > 50,20,-
둘의 차는30

두 숫자와 연산자(+,-)를 ,로 구분하여 입력 > 10,10,*
연산자는 +외 -만 지원함
'''

'''
리턴값이 여러개인데 값을 받는 변수가 1개이면 해당 변수에는 튜플형으로 값이 할당된다.
리턴값이 여러개인데 값을 받는 변수가 그 개수와 같다면 각각의 데이터형으로 값이 할당된다.
'''

def 함수_9(a):
    if a==1:
        return "리턴값은 1개 입니다"
    elif a==2:
        return "리턴값은","2개 입니다"
    elif a==3:
        return "리턴값은","3개","입니다"
    else:
        return "1~3 까지만 지원합니다."
    
print(함수_9(1))
print(함수_9(2))
print(함수_9(3))
'''
리턴값은 1개 입니다
('리턴값은', '2개 입니다')         # 변수 1개로 담으니 2개의 튜플형으로 저장됨
('리턴값은', '3개', '입니다')      # 변수 1개로 담으니 3개의 튜플형으로 저장됨
'''
