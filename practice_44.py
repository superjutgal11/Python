"""
재귀호출

재귀호출이란 함수 안에서 자기자신을 호출하는 방식을 뜻함.
보통 알고리즘 구현에서 자주 사용되며 코드는 짧지만 알고리즘적으로 매우 복잡할 수 있음.
"""

# def fun1():
#     print(10)
#     fun1()

# fun1()

"""
재귀함수의 최대 재귀 깊이는 1000이기에 1000번 넘게 자기자신을 호출할 시 에러가 발생하게 됨.
즉 반드시 재귀호출 종료조건을 만들어야 합니다.
"""

def fun2(count):
    if count<=0:
        return
    
    print("안녕하세요")
    count-=1
    fun2(count)
3
fun2(10)

"""
재귀호출로 팩토리얼을 구하는걸 직접만들어 보았다
"""

# result = 1 # 곱할 것이므로 전역변수로 초기값을 1로 설정해 둠

# def fun3(x):
#     global result
#     if x <= 0: # 종료조건 만들기
#         result = "잘못입력" 
#         return
    
#     result*=x
#     x-=1
#     if x ==0:
#         return
#     fun3(x)
    

# x = input("n팩토리얼의 n값을 입력하시오 : ")
# x = int(x)
# fun3(x)
# print("결과값은 "+str(result)+"입니다.")


# def func():
#     global a 
#     a = 10
#     return

# func()
# print(a)
# #-----------------------
# global b
# b = 10

# def func2():
#     global b
#     b = 20
#     return

# func2()
# print(b)

# def func3():
#     b = 30
#     return
# func3()
# print(b)

# a = 10

# def fun():
#     global a=10
#     return

# print()


# 내가 한게 아닌 답변 코드

def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 
print(factorial(5))

