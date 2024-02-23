# 람다 표현식

'''
람다표현식은 이름이 없는 함수를 만들기에 익명함수라고도 하며 이름이 없기에 
변수에 넣어 호출하는 방식이 많다.
람다표현식은 함수를 간편히 작성가능하여 다른 함수의 인수로 넣을 때 잘 쓴다.

람다표현식 : lambda 매개변수들 : 반환할 식
변수에 할당 : 변수 = lambda 매개변수들 : 반환할 식
'''












# # 람다 표현식 예문
# lambda a : a+10

# # 람다 표현식을 변수에 할당
# var = lambda a : a+10
# print(var(20))

# # 람다 바로 호출
# print((lambda a:a+10)(2))
# print(lambda a : a+10)

'''
람다 표현식 안에 새 변수를 만들 수 없으니 변수가 필요한 경우 def로 함수를 작성하자.
다만 외부에 있는 변수를 사용할 수는 있다
# '''
# b = 10
# print((lambda a : a+b)(10))

# map 함수 사용
'''
여러 데이터를 받아서 각각 요소에 함수를 적용한 결과를 반환하는 함수
map(함수,시퀀스 객체)
# '''

# def fun(a):
#     return a*2

# z = [1,2,3,4,5]
# x = map(fun,z)
# print(list(x))


# def func(a,b):
#     return a**2 , b**2

# a = [10,20,30,40,50]
# b = [2,3,4,5]
# ans = map(func,a,b)
# print(list(ans))


# def fun(a,b):
#     return a+10 , b+15

# a=[1,2,3]
# b=[4,5]
# ans = list(map(fun,a,b))
# print(ans)


def plus_ten(x):
     return x + 10

print(list(map(plus_ten, [1, 2, 3])))

print(list(map(lambda x: x + 10, [1, 2, 3])))