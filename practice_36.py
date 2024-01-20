# 메소드 오버라이딩

# 자식 클래스에서 정의한 메소드를 사용할 때, 메소드를 새롭게 정의하는 것을 오버라이딩이라고 함.

class Unit: 
    def __init__(self,name,hp,speed): # 스피드 추가 
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self,location): # 새로운 메소드 추가
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2}]"\
              .format(self.name,location,self.speed))

class 공격유닛(Unit): 
    def __init__(self,name,hp,speed,damage): # speed 내용 추가
        Unit.__init__(self,name,hp,speed) 
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

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도] : {2}".format(name,location,self.flying_speed))

class 비행공격유닛(공격유닛,Flyable): # 이미 스피드 관련 사항이 있으나 위 클래스에서 speed 값을 할당받고 있긴 하므로
    def __init__(self,name,hp,damage,flying_speed): 
        공격유닛.__init__(self,name,hp,0,damage) # 지상스피드는 0임을 선언해 둠
        Flyable.__init__(self,flying_speed)

# 소환
        
# 벌쳐 = 공격유닛("벌쳐",80,10,20)
# 벌쳐.move("11시")

# 배틀크루져 = 비행공격유닛("배틀크루져",500,25,3)
# 배틀크루져.fly(배틀크루져.name,"9시")

# [지상 유닛 이동]
# 벌쳐 : 11시 방향으로 이동합니다. [ 속도 : 10]
# 배틀크루져 : 9시 방향으로 날아갑니다. [속도] : 3


# 지상공격유닛과 비행공격유닛 소환인데 이러면 지상이면 .move 공중이면 .fly 를 매번 구분해서 써야함. 매우 귀찮은 일임.

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 위 코드를 그대로 가져옴

class Unit: 
    def __init__(self,name,hp,speed):  
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self,location): 
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2}]"\
              .format(self.name,location,self.speed))

class 공격유닛(Unit): 
    def __init__(self,name,hp,speed,damage): 
        Unit.__init__(self,name,hp,speed) 
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

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도] : {2}".format(name,location,self.flying_speed))

class 비행공격유닛(공격유닛,Flyable): 
    def __init__(self,name,hp,damage,flying_speed): 
        공격유닛.__init__(self,name,hp,0,damage) 
        Flyable.__init__(self,flying_speed)

    def move(self,location): # 새롭게 추가
        print("[공중유닛 이동]")
        self.fly(self.name,location)


벌쳐 = 공격유닛("벌쳐",80,10,20)
벌쳐.move("11시")

배틀크루져 = 비행공격유닛("배틀크루져",500,25,3)
배틀크루져.move("9시")

# [지상 유닛 이동]
# 벌쳐 : 11시 방향으로 이동합니다. [ 속도 : 10]
# [공중유닛 이동]
# 배틀크루져 : 9시 방향으로 날아갑니다. [속도] : 3

# 위처럼 오버라이딩을 하면 지상공격유닛이든 비행공격유닛이든 그냥 .move("로케이션 값")만으로 일치화시킬 수 있어서 편리함.