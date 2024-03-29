'''
당신은 cocoa 서비스를 이용하는 택시 기사이다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하라.

조건 1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해진다.
조건 2 : 당신은 소요 시간 5분~15분 사이의 승객만 매치할 것이다.

< 출력문 >
   [O] 1번째 손님 (소요시간 : 15분)
   [X] 2번째 손님 (소요시간 : 40분)
   [O] 3번째 손님 (소요시간 : 5분)
   ...
   [O] 50번째 손님 (소요시간 : 7분)

   총 탑승 손님 = 3 명
'''



# 내가 작성한 코드 

from random import *

총_탑승손님 = 0
for 손님_매칭_번호 in range(1,51) :
    손님별_걸리는_시간 = int(random()*46)+5
    if 손님별_걸리는_시간 <= 15 :
        총_탑승손님 += 1
        탑승여부 = "O"
    else:
        탑승여부 = "X"
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(탑승여부,손님_매칭_번호,손님별_걸리는_시간))
print("총 탑승 손님 : {0} 명".format(총_탑승손님))



# 나노코딩이 작성한 코드

cnt = 0 # 총 탑승 승객
for i in range(1,51):
    time = randrange(5,51) # 5부터 51 미만(50까지)의 정수형 난수 생성
    if 5<= time <=15: # 5~15분의 손님
        print("[O] {0}번째 손님 (소요시간 = {1})".format(i,time))
        cnt+=1
    else: # 매칭 실패이므로 cnt 증가는 없음
        print("[X] {0}번째 손님 (소요시간 = {1})".format(i,time))
print("총 탑승 승객 : {0} 명".format(cnt))