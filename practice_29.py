# pickle , with

# -----------------------------------------------------------------------------------------------------------

# pickle : 파이썬에서 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 것을 뜻함

import pickle

profile_file = open("profile.pickle","wb") # 쓰기 목적으로 w , b는 바이너리타입을 정의함을 의미. 
# 피클을 쓸 때 반드시 바이너리타입임을 정의해야 하며, 따로 인코딩 정의는 필요가 없다.
profile = {"이름":"정재형","나이":23,"취미":["코딩","여행","음악 감상"]}
print(profile)
pickle.dump(profile,profile_file) # profile에 있는 정버를 profile_file 에 저장.
profile_file.close()
# {'이름': '정재형', '나이': 23, '취미': ['코딩', '여행', '음악 감상']}
# 위가 출력됨과 동시에 profile.pickle 이라는 이름의 파일이 생김.

# 위 파일에서 데이터를 가져오는 예제
profile_file = open("profile.pickle","rb") # 쓰기아니고 읽기 + 바이너리
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile 에 불러오는 코드
print(profile)
profile_file.close()

# -----------------------------------------------------------------------------------------------------------

# with를 쓰면 파일을 열고 처리하고 닫는 작업을 더 쉽게 할 수 있다.

import pickle

with open("profile.pickle","rb") as profile_file: # profile.pickle 파일을 rb 목적으로 열어서 profile_file 에 저장하고
    print(pickle.load(profile_file)) # profile_file 의 내용을 pickle.load 를 통해 불러와서 print 해 준다.

# 출력 : {'이름': '정재형', '나이': 23, '취미': ['코딩', '여행', '음악 감상']}
# with 문의 경우에는 파일을 close로 닫아줄 필요가 없이 with문 탈출하며 자동으로 닫아준다.

# pickle 이 아닌 일반적인 파일을 쓰고 읽는 것을 with문을 통해 해 보면

with open("study.txt","w",encoding="utf8") as study_file: # pickle이 아니므로 그냥 w 만 작성
    study_file.write("파이썬을 열심히 공부하고 있어요.")

# 위 코드를 실행하면 study.txt 라는 파일이 생성되고 들어가 보면 [파이썬을 열심히 공부하고 있어요.] 라는 내용이 작성 돼 있다.
    

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

# 파이썬을 열심히 공부하고 있어요.
# 위위 문장, 위 문장 둘 다 단 2줄만으로 파일의 쓰고 불러오는 작업을 할 수 있다. close 안해도 되는 장점도 있다.