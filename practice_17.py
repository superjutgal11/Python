# 사전자료형


# 사전에서는 한 단어와 그 단어의 뜻이 같이 나오게 된다. 코딩에서 문자사전형은 key 와 value 가 나오게 된다.
# key는 해당 사물함만 열 수 있고 중복을 허용하지 않는다. 


# 사전의 형식은 { key : value } 
cabinet = {3:"재형",100:"원영"} # 3번째 열쇠는 재형이, 100번째 열쇠는 원영이 쓰고 있다.
print(cabinet) # 출력은 { key_1 : value_1 , key_2 : value_2 } 이런 식이다.
# 윗 줄의 출력 = {3: '재형', 100: '원영'}


# 사전자료형에서 값을 가져오는 방법은 2가지가 존재한다.
print(cabinet[3]) # 재형
print(cabinet[100]) # 원영
# 위처럼 대괄호로 가져오는 방법과
print(cabinet.get(3)) # 재형
print(cabinet.get(100)) # 원영
# 위처럼 .get(key) 방법이 있다.


# 만약에 key 가 없는데 값을 가져오게 되면 cabinet[key] 형태나 .get(key) 형태에 따라 출력이 달라진다.
# 첫번째로 cabinet[key] 형태로 하면 
'''
print(cabinet[5])
print("hi")
'''
# KeyError: 5 가 출력되며 어디가 오류인지 알려주고, 뒤 코드 실행하지 않은 채 바로 프로그램을 종료시킨다.
# 두번째로 get.(key) 형태로 하면 
print(cabinet.get(5))
print("hi")
# 프로그램 오류 없이 None 문자만 출력하고 뒤의 코드들도 실행된다.
# 만약 .get(key)가 None인 상태, 즉 key가 설정되지 않은 상태일 때 기본값을 쓰고 싶다면
print(cabinet.get(5,"사용가능합니다."))  # 사용가능합니다. None은 출력되지 않고 뒤 값이 출력. 
print(cabinet.get(5,10))  # 이렇게 하면 None은 출력되지 않고 기본값으로 지정된 10 만 출력됨.


# "key in 변수" 처럼 in을 이용하여 사전자료형에 자료가 있는지 확인할 수 있다. 출력값은 부울이다.
print(3 in cabinet) # key 3에 자료 있으므로 True
print(5 in cabinet) # key 5에 자료 없으므로 False


# 또한 위에선 key를 정수로 했지만 String 형으로도 가능하다.
cabinet = {"A-1":"정재형","A-2":"장원영"}
print(cabinet["A-1"])
print(cabinet.get("A-2"))


# 새 손님이 와서 새로운 key에 값(value)를 넣으려면
cabinet["A-3"] = "카리나"
print(cabinet.get("A-3"))
# 만약 새로운 값을 넣을 때 이미 값이 있던 key 라면 그 값은 업데이트 되는 것이다.
cabinet["A-3"] = "화사"
print(cabinet) # {'A-1': '정재형', 'A-2': '장원영', 'A-3': '화사'}


# 간 손님이 있다면 "del 변수[key]" 로 지울 수 있다.
del cabinet["A-2"] # 왜인지 del cabinet.get("A-2")로 하면 오류가 발생한다.
print(cabinet) # {'A-1': '정재형', 'A-3': '화사'} 


# 사용중인 key만을 출력
print(cabinet.keys()) # 출력 = dict_keys(['A-1', 'A-3'])

# 사용중인 value만을 출력
print(cabinet.values()) # 출력 = dict_values(['정재형', '화사'])

# 사용중인 key들과 value들을 쌍으로 출력
print(cabinet.items()) # dict_items([('A-1', '정재형'), ('A-3', '화사')])

# key와 value값들을 모조리 void로 만들기 (ex.지하철 영업종료)
cabinet.clear()
print(cabinet) # 출력 = {}