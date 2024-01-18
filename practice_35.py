# 다중 상속

# 부모 클래스 : 상속하는 클래스. 데이터/메소드를 제공해 주는 클래스.
# 자식 클래스 : 상속받는 클래스. 데이터/메소드를 제공 받는 클래스.
# 다중 상속 : 여러 부모 클래스를 갖는 경우.

class Unit: 
    def __init__(self,name,hp): 
        self.name = name
        self.hp = hp

class 공격유닛(Unit): 
    def __init__(self,name,hp,damage): 
        Unit.__init__(self,name,hp) 
        self.damage = damage 

    def attack(self,location): 
        print("{0} : {1} 방향으로 공격합니다. [ 공격력 = {2} ]".\
              format(self.name,location,self.damage))
    
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 갖는 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도] : {2}".format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스
class 비행공격유닛(공격유닛,Flyable): # 다중 상속 받을 때는 () 안에 , 로 구분하여 상속받을 부모 클래스들을 넣는다.
    def __init__(self,name,hp,damage,flying_speed): # 즉 위의 두 클래스의 모든 변수/함수 전부 사용 가능!!
        공격유닛.__init__(self,name,hp,damage) # 전체적으로 초기화 해 주기
        Flyable.__init__(self,flying_speed)

발키리 = 비행공격유닛("발키리",200,6,5)
발키리.fly(발키리.name,"3시") # Flyable 의 fly 함수를 호출
# 출력 = 발키리 : 3시 방향으로 날아갑니다. [속도] : 5

'''

비행공격유닉 ----> 공격유닛 ----> Unit
         ㄴ---> Flyable

이런 식으로 다중상속이 이뤄져 있음.

'''