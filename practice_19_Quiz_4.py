'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 한명은 1명은 치킨 쿠폰, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하십시오.

조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정.
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복불가(치킨-커피 공동수령 불가).
조건 3 : random 모듈의 shuffle과 sample을 활용.

[출력 예제]
-- 당첨자 발표 --
치킨 쿠폰 당첨자 : 1
커피 쿠폰 당첨자 : [2, 3, 4]
-- 축하합니다 --

[shuffle 사용법]
1st = [1,2,3,4,5]
shuffle(1st)
하면 1st 내의 값들의 위치가 완전 랜덤으로 서로 섞이게 됨.

[sample 사용법]
1st = [1,2,3,4,5]
print(sample(1st,1))
하면 1st의 값들 중 무작위로 1개를 뽑게 된다.
'''

# 위 글에서 출력에제가 [] 리스트형식이기에 참여자_id를 리스트형태로 만들었다.

# 작성코드 1 _ sample 만을 사용
from random import*
참여자_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 순서를 갖는 리스트형 변수 선언.
당첨자_최초 = sample(참여자_id,4) # 20명 중 우선 치킨 1명 + 커피 3명 총 4명을 1차 선발한다. 리스트형으로 저장될 것.
당첨자_치킨 = 당첨자_최초[0]
당첨자_커피 = [당첨자_최초[1],당첨자_최초[2],당첨자_최초[3] ]
print("-- 당첨자 발표 --")
print("치킨 쿠폰 당첨자 = "+str(당첨자_치킨))
print("커피 쿠폰 당첨자 = "+str(당첨자_커피))
print("-- 축하합니다 --")

# 작성코드 2 _ shuffle 만을 사용
참여자_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(참여자_id) 
당첨자_치킨 = 참여자_id[0]
당첨자_커피 = [참여자_id[1],참여자_id[2],참여자_id[3] ]
print("-- 당첨자 발표 --")
print("치킨 쿠폰 당첨자 = "+str(당첨자_치킨))
print("커피 쿠폰 당첨자 = "+str(당첨자_커피))
print("-- 축하합니다 --")

# 작성코드 3 _ shuffle과 sample을 둘 다 활용.. 솔직히 하나만 해도 충분한데..
참여자_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(참여자_id)
당첨자_치킨 = sample(참여자_id,4)
당첨자_치킨 = 참여자_id[0]
당첨자_커피 = [참여자_id[1],참여자_id[2],참여자_id[3] ]
print("-- 당첨자 발표 --")
print("치킨 쿠폰 당첨자 = "+str(당첨자_치킨))
print("커피 쿠폰 당첨자 = "+str(당첨자_커피))
print("-- 축하합니다 --")



# 나노코딩이 작성한 답변

# 리스트 만들 때 users = [1 , 2 , ...] 이런 것보단 range(a,b) 이렇게 하면 a 부터 (b-1)까지 숫자를 생성하게 된다.
users = range(1,21) # 1부터 20까지의 리스트를 users 변수에 저장
# type() 명령어로 타입을 확인하면
print(type(users)) # <class 'range'> 즉 리스트형이 아닌 레인지형식이고 이러면 리스트형의 함수를 쓸 수가 없음.
print(users) # 레인지형은 출력이 range(1, 21) 이렇게 나오는구만
users = list(users) # 리스트형 명령어 사용을 위해 타입을 리스트형으로 바꿔 준다
print(type(users)) # <class 'list'>
print(users) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 리스트로 잘 만들어짐를 확인한다.

shuffle(users) # 위 리스트를 잘 섞어준다
# 무작위로 중복없이 뽑아야 함. 즉 한번에 4명을 다 뽑는것으로 함.
winners = sample(users,4) # users 리스트에서 랜덤으로 4명 뽑음. 솔직히 이럴거면 shuffle 필요없긴 함.

print("-- 당첨자 발표 --")
print("치킨 쿠폰 당첨자 = {0}".format(winners[0]))
print("커피 쿠폰 당첨자 = {0}".format(winners[1:]))
print("-- 축하합니다 --")