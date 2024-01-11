'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하십시오.

예시 ) http://naver.com
규칙_1 : http:// 부분은 제외 => naver.com
규칙_2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙_3 : 남은 글자 중 처음 세자리 + 규칙 2의 글자 갯수 + 규칙 2의 글자 내 'e' 갯수 + "!" 로 구성
결과적으로 생성된 비밀번호 ) nav51!
'''


# 내가 만든 프로그램. pw를 만드려고 하는 사이트의 링크르 website 변수에 넣어서 실행하라.
# 하나의 제작 코드로 각각 네이버/다음/구글 주소를 website 변수에 넣어 각각 비밀번호를 생성하였다.

website = "http://naver.com"                                # website = 입력받을 웹 사이트 원래 주소
era_web_1 = website.replace("http://","")                   # era_web_1 = 위의 주소에서 era_web_1 = http:// 를 제거한 주소
pos_poi = era_web_1.index(".")                              # pos_poi = .의 인덱스
era_web_2 = era_web_1[0:pos_poi]                            # era_web_2 = 인덱스 0부터 ( pos_poi - 1 ) 위치까지만의 주소
pw_bs = era_web_2[0:3]                                      # pw_bs = 위 주소에서 인덱스  0 ~ 2 까지 앞 3자리 주소만 받아 옴
le_pw = len(era_web_2)                                      # le_pw = era_web_2 의 길이 정수를 저장
pw_cp = f"{pw_bs}{le_pw}{era_web_2.count("e")}!"            # pw_cp = 최종 비밀번호를 조합
print(f"{website}주소에서 사용하실 비밀번호는 {pw_cp}입니다.")       # pw_cp를 출력

website = "http://daum.net"
era_web_1 = website.replace("http://","")
pos_poi = era_web_1.index(".")
era_web_2 = era_web_1[0:pos_poi]
pw_bs = era_web_2[0:3]
le_pw = len(era_web_2)  
pw_cp = f"{pw_bs}{le_pw}{era_web_2.count("e")}!"
print(f"{website}주소에서 사용하실 비밀번호는 {pw_cp}입니다.")

website = "http://google.co.kr"
era_web_1 = website.replace("http://","")
pos_poi = era_web_1.index(".")
era_web_2 = era_web_1[0:pos_poi]
pw_bs = era_web_2[0:3]
le_pw = len(era_web_2)  
pw_cp = pw_bs + str(le_pw) + str(era_web_2.count("e")) + "!" 
print(f"{website}주소에서 사용하실 비밀번호는 {pw_cp}입니다.")

# 헷갈렸던 거
# pw_cp = f"{pw_bs}{era_web_2.count("e")}!"
# 이 부분에서 f 뒤에 ( ) 를 친다거나, "" 을 전체적으로 덮는 등의 실수를 함
# pw_cp = pw_bs + le_pw + era_web_2.count("e") + "!" 
# 위 코드가 왜 안되나 했더니 + 로 연결된 경우 str 형이 아닌 경우 모두 str() 를 씌어야 함을 잊고 있었음
# pw_cp = pw_bs + str(le_pw) + str(era_web_2.count("e")) + "!"      로 하면 해결됨


# 나노코딩이 작성한 답변

ur1 = "http://naver.com"
my_str = ur1.replace("http://","")  # 규칙 1 적용
my_str = my_str[:my_str.index(".")] # 슬라이싱 이용하여 . 이후 부분은 삭제
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(ur1,password))