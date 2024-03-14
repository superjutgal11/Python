# 클래스를 선언하고 실행하는 과정에서 하나 짚고 가야 할 것 같습니다.
# 우선 아래의 코드는 실행됩니다.

class jjh:
    def a(a1,b1):
        print(a1,b1)

    def b(a2,b2):
        print(a2,b2)

jjh.a(20,30)
jjh.b(50,60)

# 하지만 다음처럼하면 오류가 발생합니다.

"""
class jjh:
    def a(self,a1,b1):
        print(a1,b1)

    def b(self,a2,b2):
        print(a2,b2)

jjh.a(20,30)
jjh.b(50,60)
"""

# 클래스의 메소드의 첫 인자는 self 여야 한다고 했는데 오류가 발생한 이유에 뭘까??

# 우선 클래스.메소드(인자) 는 단순히 해당 클래스 내부의 메소드를 빌려 사용하는 것이고,
# self인자는 객체를 만들 때 사용하는 것이다. 즉 self로 접근하고싶다면 인스턴스를 만들어야 한다. 예를 들어
class 테스트:
    def 함수_1(self,a,b):
        print(a,b)

    def 함수_2(self,c,d):
        print(2*c,3*d)

객체_1 = 테스트() # 테스트 클래스의 객체를 생성함.
a = 객체_1.함수_1(10,10)
b = 객체_1.함수_2(10,10)
print(a,b,sep="    ")

# 여기서 또 헷갈렸던 것,
# 위 코드의 출력이
'''
20 30
50 60
10 10
20 30
None    None
'''
# 인데 None None 이 뜨는 이유를 알아야 한다.
# 우선 return값이 없는 상태이므로 print문이 종료되면 바로 탈출하고, 반환값이 없기에 a와 b에 할당치가 없는 None이 들어간다.
# 즉 각각 함수에 들어가 출력은 하되, 리턴값은 없으므로 정상적인 출력 이후 None 이 출력되었다.

# 클래스 내부의 함수와 클래스 외부의 함수를 구분하여 사용하도록 연습하자.

class A : 
    def __init__(self):
        pass

    def a(self):
        print("hi")

    def b(self):
        self.a()

    def c(self):
        a()

def a():
    print("hello!!!!!!!")

객체 = A()
객체.b()
객체.c()
a()

# 다음의 출력값은 다음과 같다.
# 출력된 루틴을 따라가 보자. 인스턴스b > 클래스함수a > hi 출력 , 인스턴스c > 외부함수 a > hello 출력 ,
# 외부함수 a 출력 > hello 출력