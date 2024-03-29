# 16강 _ 리스트

# 리스트 = 순서를 가지는 객체의 집합
# 예를들어 지하철 각 차에 10명, 20명, 30명이 탄다고 가정하면 각각 변수에 수를 할당 시
'''
subway1 = 10
sybway2 = 20
subway3 = 30
'''
# 이런 식으로 해야 할 것이다. subway 하는 리스트를 만들면 더 간단히 묶음을 만들 수 있다.
subway = [10,20,30]
print(subway)  # 출력 = [10, 20, 30]  데이터가 [ ] 사이에 묶여서 출력됨

# 응용 : 다음과 같이 지하철 칸에 사람들이 앉아있을 때 정지호 는 몇번째 칸에 앉아있는가?
subway = ["정재형" , "정지호" , "장지홍"]
print(subway)  # ['정재형', '정지호', '장지홍']
print(subway.index("정지호"))  # 1번 인덱스임을 출력

# 응용 : 다음 정류장에 위 지하털에 "정형"이가 승차함. 서브웨이 리스트에 추가하면 ?
subway.append("카리나")  # append 는 리스트 맨 뒤에 추가하는 명령어임.
print(subway) # ['정재형', '정지호', '장지홍', '카리나']

# 응용 : 이번엔 '정재형'과 '정지호' 가운데에 "장원영"을 추가 해 보자.
subway.insert(1,"장원영")  # insert로 인덱스 1 에 '장원영'을 넣고 그 뒤 리스트는 뒤로 밀기
print(subway) # ['정재형', '장원영', '정지호', '장지홍', '카리나']

# 응용 : pop 명령어는 뒤에서부터 하나씩 꺼내오는 명령어
print(subway.pop()) # 이렇게 하면 맨 뒤 사람이 누군지 알 수 있다. 카리나 출력됨
print(subway) # ['정재형', '장원영', '정지호', '장지홍']

print(subway.pop()) # 장지홍
print(subway) # ['정재형', '장원영', '정지호']

print(subway.pop()) # 정지호 
print(subway) # ['정재형', '장원영']

# 다른 지하철이 왔다.
subway_2 = ["피카츄","파이리","꼬렛","루주라","꼬렛","꼬렛","피카츄","잉어킹"]
# 같은 이름의 객체가 몇 개 있는지 확인 해 보자. 각각 3 , 2 가 나온다.
print(subway_2.count("꼬렛"))
print(subway_2.count("피카츄"))

# 정렬 가능
num_list = [5,2,3,0,7,11,2]
num_list.sort() # 여기에서 num_list 객체가 작은 수부터 큰 수로 정렬됨
print(num_list) # [0, 2, 2, 3, 5, 7, 11]

# 뒤집기 기능
num_list.reverse() # # 여기에서 num_list 객체 순서가 완전히 뒤집어짐
print(num_list) # 여기에선 큰 수부터 작은 수대로 나열하게 됨. [11, 7, 5, 3, 2, 2, 0]

# 리스트의 모든 객체 지우기
num_list.clear()  # 모든 객체 없어짐
print(num_list)  # 출력이 [] 로 나옴

# 리스트는 자료형에 영향없이 섞어서 사용이 가능함
mix_list = ["정재형",True,34,-9.44]
print(mix_list)  # 출력 = ['정재형', True, 34, -9.44]

# 서로 다른 리스트들을 서로 확장할 수 있음
num_list_0 = [4,0,11]
num_list_1 = [9,1,2,4]
num_list_0.extend(num_list_1) # num_list_0 과 num_list_1 가 확장된 후, num_list_0 에 저장됨.
print(num_list_0)  # [4, 0, 11, 9, 1, 2, 4]