# super

class Unit: 
    def __init__(self,name,hp,speed): 
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self,location): 
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2}]"\
              .format(self.name,location,self.speed))

class 건물건축(Unit):
    def __init__(self,name,hp,location):
        # Unit.__init__(self,name,hp,0) # 건물은 이동하지 않으므로 스피드 0 넣음. 이렇게 하는 방법도 있고
        super().__init__(name,hp,0) # super를 통해 초기화 시 self 정보는 적지 않음.
        # 유닛 클래스(부모 클래스)에 대해 자신이 상속받는 변수를 초기화 할 수 있다.

# 문제는 다중 상속에서 발생함. 새롭개 코드를 짜 보자.
        
class 유닛:
    def __init__(self):
        print("유닛 생성자")

class 비행가능:
    def __init__(self):
        print("비행가능 생성자")

class 비행가능유닛(유닛,비행가능): # 다중 상속
    def __init__(self):
        super().__init__() # self는 받는게 없으니 괄호 그냥 닫기

드랍쉽=비행가능유닛()
# 출력 = 유닛 생성자
# 즉 위에서 유닛만 받아 옴. 만약 순서를 바꾼다면

class 비행가능유닛_2(비행가능,유닛): # 다중 상속
    def __init__(self):
        super().__init__() # self는 받는게 없으니 괄호 그냥 닫기

드랍쉽=비행가능유닛_2()
# 출력 = 비행가능 생성자
# 순서를 바꿨더니 이번엔 첫번째 인자가 출력됨.
# 즉 두개 이상의 부모클래스로부터 다중상속 시 맨 처음 인자의 클래스만 호출이 된다.
# 즉 다중상속을 하며 여러 클래스로부터의 변수 초기화가 필요할 때는 따로 명시 해 주자.
# 예를들어 유닛.~~ 비행가능.~~ 아런식으로