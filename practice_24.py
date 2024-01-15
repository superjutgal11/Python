# 함수 호출 방법 , 지역변수 , 전역 변수

"""
    함수 호출 방법

    1. 키워드를 이용한 함수 호출법
    여러개의 매개변수가 있는 함수에서 매개변수의 순서를 고려하지 않고 키워드를 선택해 함수를 호출.
    
    2. 가변인자를 이용한 함수 호출법
    각기 다른 갯수의(가변의) 매개변수를 호출하는 방법.
"""

# 1. 키워드를 이용한 함수 호출법 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def profile(name,age=25,main_language='python'):
     print("이름 = {0}\t나이 = {1}\t메인랭귀지 = {2}".format(name,age,main_language))
profile("정재형",23,"java")
profile("카리나",25,"python")

# 만약 위같이 여러개의 매개변수가 있을 때 매개변수의 순서를 고려하지 않고 선택하여 매개변수를 초기화 하려면
profile(name="박의진",main_language="C# and C")

# 이런 식으로 각각 매개변수에 접근해야 한다.
# 만약 profile("박의진", ,'C++')로 하면 접근 오류, profile("박의진", None, 'C++') 로 하면
# age에 None 값이 할당되어 원하는 결과가 나지 않는다.

profile(main_language="Java_script" , name = "윈터" , age = 19)
# 출력 =  이름 = 윈터     나이 = 19       메인랭귀지 = Java Script
# 또한 위처럼 직접 각각 변수에 값을 넣는 경우에는 순서는 상관이 없다.


# 2. 가변인자를 이용한 함수 호출법 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def profile(name,age,len_1,len_2,len_3,len_4,len_5):
     print("이름 : {0} , 나이 : {1}".format(name,age), end="  ")
     print(len_1,len_2,len_3,len_4,len_5)
# 원래 프린트문은 실행 이후 자동으로 다음줄부터 다음 명령들을 실행하게 하지만, end로 하면 자동으로 내려가지 않고
# 아래 코드에서 보이듯 end 옆 "" 의 내용을 출력한 후 이어붙어 출력시키도록 한다. 25와 C 사이 띄어쓰기가 그것.

profile("정재형",25,"C","Java","R_language","Python","Pytorch")
# 출력 = 이름 : 정재형 , 나이 : 25  C Java R_language Python Pytorch
# 프로필 함수에는 총 5개의 매개변수를 받는데, 만약 어떤 사람은 위와 달리 2개의 언어밖에 다룰 수 없다면??
# 두가지 방법으로 나머지 매개변수는 공백으로 만들 수 있다.
profile("카리나",30,"Kotlin","Swift","","","")
# 출력 = 이름 : 카리나 , 나이 : 30  Kotlin Swift 
# 그 첫번째 방법인데 앞으로 수많은 사람들을 귀찮게 이렇게 하기는 싫기 때문에 가변인자법을 사용하자.

def profile(name, age, *가능언어):     # * 를 통하여 가변 인자를 생성할 수 있다.
     print("이름 : {0} , 나이 : {1}".format(name,age), end="  ")
     for i in 가능언어:
          print(i,end = "  ")
          
profile("정재형",23,"C_language","Java","Python","Matlab","R_language")
print() # 이 문장으로 각각 객체를 띄어쓰기로 구분
profile("카리나",29,"C++","C#")
print() 
profile("지젤",29,"TensorFlow","C#","mySQL","AWS")
print() 

# 출력

# 이름 : 정재형 , 나이 : 23  C_language  Java  Python  Matlab  R_language  
# 이름 : 카리나 , 나이 : 29  C++  C#  
# 이름 : 지젤 , 나이 : 29  TensorFlow  C#  mySQL  AWS 

# 각기 다른 갯수의 매개변수가 삽입되어 출력됨을 확인할 수 있다!!


'''
지역 변수 : 함수 호출 시 만들어졌다가 호출이 끝나면 사라지는 함수 내에서만 쓸 수 있는 변수.
전역 변수 : 프로그램 내에서 어디든지 호출 가능한 변수.
'''

# gun = 10
# def 체크포인트(soilders):
#      gun -= soilders
#      print('[함수 내] 남은 총 : '+str(gun))

# print("전체 총 : "+str(gun))
# 체크포인트(2)
# print("남은 총 : ".format(gun))

# 위 코드는 실행이 되지 않는다. 체크포인트 함수 내에 선언된 gun은 [체크포인트]함수에서만 쓸 수 있는 지역변수인데 
# 초기화가 안 돼 있기에 쓸 수 없다는 뜻임. 함수 내에 있는 gun과 밖에 있는 gun은 다름.
# 헷갈리면 이리 생각하자. 함수 내 지역변수가 바뀐다고 전역변수 값도 바뀌지 않음. 즉 함수 입장 전역변수는 사실 상수임.
# 즉 위같은 연산을 하고싶다면 새로운 지역변수를 선언하고 연산하는게 맞음. 예를 들어

gun = 10
def 체크포인트(soilders):
     gun = 10 # 지역변수로서 함수 내에 gun을 선언 해 준다
     gun -= soilders
     print('[함수 내] 남은 총 : '+str(gun))

print("전체 총 : "+str(gun))
체크포인트(2)
print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 10

'''
만약 함수 내에서 전역변수를 쓰고 싶다면 global 을 쓰면 된다.
'''

gun = 10
def 체크포인트(soilders):
     global gun  # 체크포인트 함수에서 gun은 전역변수 gun을 쓴다를 선언함
     gun -= soilders  
     print('[함수 내] 남은 총 : '+str(gun))
print("전체 총 : "+str(gun))
체크포인트(2)
print("남은 총 : {0}".format(gun))  # 전역변수기에 함수 외부에서도 gun값이 함수에 따라 바뀜.

# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

# 하지만 코드가 많아지면 위의 global 방식은 가독성이 크게 떨어져서 권장되지 않는다.
# 그래서 아래와 같은 식으로 많이 쓰게 됩니다.


gun = 10
def 체크_2 (gun,soilder):  # 매개변수도 지역변수임
     gun = gun - soilder  # 즉 여기서 값이 바껴도 전역변수값이 바뀌지는 않음.
     print('[함수 내] 남은 총 : '+str(gun))
     return gun  # 리턴을 통해 함수 안의 결과치를 끄집어 냄
gun = 체크_2 (gun,2)  # 끄집어 낸 값을 함수 밖 전역변수이 gun에 넣음
print("남은 총 : {0}".format(gun)) 

# 남은 총 : 8
# [함수 내] 남은 총 : 8
# 남은 총 : 8