# pass 

class Unit: 
    def __init__(self,name,hp,speed):  
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self,location): # 새로운 메소드 추가
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 : {2}]"\
              .format(self.name,location,self.speed))

class 건물건축(Unit):
    def __init__(self,name,hp,location):
        pass

서플라이_디포=건물건축("서플라이 디포",500,"북동쪽")

# 이렇게 하면 일단 오류 없이 프로그램이 정상적으로 종료된다.
# pass 는 아무것도 안하고 일단 그냥 넘어간다는 의미이다.

def 게임시작():
    print("[알람] 새로운 게임을 시작합니다.")

def 게임종료():
    pass

게임시작()
게임종료()

# [알람] 새로운 게임을 시작합니다.  출력은 게임시자만 됨.