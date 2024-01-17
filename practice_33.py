# 클래스 내 메소드

class Unit: 
    def __init__(self,name,hp,damage): 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}  ,  공격력 : {1}".format(self.hp,self.damage))

# self 는 자기자신을 의미하며, 클래스 내에서 메소드 인자로 반드시 들어간다. def __init__(self... 처럼

class attack_unit:
    def __init__(self,name,hp,damage): 
        self.name = name # 뒤에 self가 없는 변수는 위에서 전달받은 인자를 의미함. self.name은 클래스 내에서 정의된 변수를 쓰는 것.
        self.hp = hp
        self.damage = damage

    def attack(self,location): # 로케이션은 여기서 받은 인자를 넣고 나머지는 클래스 내의 변수를 쓴다.
        print("{0} : {1} 방향으로 공격합니다. [ 공격력 = {2} ]".\
              format(self.name,location,self.damage))
    
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} 파괴되었습니다.".format(self.name))

파이어뱃 = attack_unit("파이어뱃",50,16)
파이어뱃.attack("5시")

# 데미지를 두 번 받았다
파이어뱃.damaged(25) # 체력 50 > 25
파이어뱃.damaged(25) # 체력 25 > 0 (파괴)

'''
파이어뱃 : 5시 방향으로 공격합니다. [ 공격력 = 16 ]
파이어뱃 : 25 데미지를 입었습니다.
파이어뱃 : 현재 체력은 25입니다.
파이어뱃 : 25 데미지를 입었습니다.
파이어뱃 : 현재 체력은 0입니다.
파이어뱃 파괴되었습니다.
'''