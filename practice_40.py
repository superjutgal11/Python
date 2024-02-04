# 스타크래프트 텍스트기반 프로젝트_2

# 후반전

from random import*

class 유닛: 
    def __init__(self,name,hp,speed): 
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(self.name))
    
    def 지상이동(self,location): 
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2}]"\
              .format(self.name,location,self.speed))
    
    def 피해(self,damage): # 공격유닛 클래스에 있던 메소드를 여기로 옮겨 주었다
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} 파괴되었습니다.".format(self.name))
        
class 공격유닛(유닛): 
    def __init__(self,name,hp,speed,damage): # speed 내용 추가
        유닛.__init__(self,name,hp,speed) 
        self.damage = damage 

    def 공격(self,location): 
        print("{0} : {1} 방향으로 공격합니다. [ 공격력 = {2} ]".\
              format(self.name,location,self.damage))
    
class 마린생성(공격유닛):
    def __init__(self):
        공격유닛.__init__(self,"마린",40,1,5)

    def 스팀팩(self):
        if self.hp > 10 :
            self.hp -= 10
            print("{0}이 스팀팩을 사용합니다. 체력이 10 감소합니다.".format(self.name))
        else:
            print("{0}의 체력이 부족하여 스팀팩을 사용할 수 없습니다. 현재체력 : {1}".format(self.name,self.hp))

class 탱크생성(공격유닛): # 시즈모드가 있는 유닛
    시즈모드_개발=False # 시즈모드 업글 했는지 여부

    def __init__(self):
        공격유닛.__init__(self,"탱크",150,1,35)
        self.시즈모드=False # 초기값은 시즈모드상태가 아님으로 정의

    def 시즈모드(self):
        if 탱크생성.시즈모드_개발==False:
            return
        
        if self.시즈모드_개발==True: # 현재 상태가 시즈인지 시즈가 아닌지 여부에 따라 분기 필요
            if self.시즈모드==False:
                print("{0}가 시즈모드로 전환합니다.".format(self.name))
                self.damage*=2
                self.시즈모드==True
            else:
                print("{0}가 일반모드로 전환합니다.".format(self.name))
                self.damage/=2
                self.시즈모드==False

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도] : {2}".format(name,location,self.flying_speed))

class 비행공격유닛(공격유닛,Flyable): # 이미 스피드 관련 사항이 있으나 위 클래스에서 speed 값을 할당받고 있긴 하므로
    def __init__(self,name,hp,damage,flying_speed): 
        공격유닛.__init__(self,name,hp,0,damage) # 지상스피드는 0임을 선언해 둠
        Flyable.__init__(self,flying_speed)

class 레이스(비행공격유닛): # 클로킹 모드가 있는데 여기선 개발없이 클로킹이 가능하다고 가정함
    def __init__ (self):
        비행공격유닛.__init__(self,"레이스",80,20,5)
        self.객체별_클로킹=False
    
    def 클로킹(self):
        if self.객체별_클로킹 == True:
            print("{0}의 클로킹을 해제합니다.".format.name)
            self.객체별_클로킹=False
        else:
            print("{0}의 클로킹을 실행합니다.".format.name)
            self.객체별_클로킹=True

def 게임시작():
    print("[알림] 새로운 게임이 시작되었습니다.")

def 게임종료():
    print("[알림] 게임이 종료되었습니다.")

# 게임 진행

게임시작()

마린_1 = 마린생성()
마린_2 = 마린생성()
마린_3 = 마린생성()

탱크_1 = 탱크생성()
탱크_2 = 탱크생성()

레이스_1 = 레이스()

# 일일히 생성하기 힘드므로 일괄 관리를 해 보면

유닛공격_리스트 = []
유닛공격_리스트.append(마린_1)
유닛공격_리스트.append(마린_1)
유닛공격_리스트.append(마린_3)
유닛공격_리스트.append(탱크_1)
유닛공격_리스트.append(탱크_2)
유닛공격_리스트.append(레이스_1)

# 만든 유닛 전부를 특정방향으로 이동하고자 한다면

for 생성유닛 in 유닛공격_리스트:
    생성유닛.지상이동("1시")

# 탱크 시즈모드 개발
    
시즈모드_개발 = True
print("[알림] : 탱크 시즈모드의 개발이 완료되었습니다.")

# 공격 모드 준비. 탱크 = 시즈모드 , 레이스 = 클로킹 , 마린 = 스팀팩

for 생성유닛 in 유닛공격_리스트:
    if isinstance(유닛,마린생성): # 현재 객체가 어떤 클래스의 인스턴스인지를 확인하는 명령어. isinstance 
        생성유닛.스팀팩()
    elif isinstance(유닛,탱크생성):
        생성유닛.시즈모드()
    elif isinstance(유닛,레이스):
        생성유닛.클로킹()
    
# 전군 공격 시키기

for 생성유닛 in 유닛공격_리스트 :
    생성유닛.공격("1시")

# 전군 피해
# 난수로 입는 데미지를 설정
    
for 생성유닛 in 유닛공격_리스트:
    생성유닛.피해(randint(5,20))

# 게임종료
게임종료()ㄴㄴ