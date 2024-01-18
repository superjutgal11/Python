# 상속

# 일반 유닛을 생성하는 클래스인데 매딕같은 비공격 유닛을 만들기 위해 우선 데미지 함수를 없애 보았다.
class Unit: 
    def __init__(self,name,hp): 
        self.name = name
        self.hp = hp

# 위 클래스는 아래 클래스와 멤버변수가 곂침(hp와 name). 이럴 때 상속을 쓸 수 있음.
class attack_unit(Unit): # 이렇게 ( ) 안에 상속받을 대상을 쓰면 됨.
    def __init__(self,name,hp,damage): 
        Unit.__init__(self,name,hp) # name과 hp는 Unit으로부터 상속받을 수 있기 때문에 해당 변수들은 없애고 받아올 내용을 작성
        self.damage = damage # 위 두 변수는 다른 클래스에서 받아오고, 데미지는 여기서 생성함.

    def attack(self,location): 
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