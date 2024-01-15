# 파일 입출력

# 컴퓨터에 있는 수많은 파일을 파이썬을 통해 파일을 열어서 보거나 파일을 쓸 수 있음.


#-----------------------------------------------------------------------------------------------------------


'''
score_file = 변수 이름
open() = 파일을 여는 명령어
open("파일 이름","w",encoding = "utf8")
    ㄴ 에서 "w" 는 쓰기위한 목적(덮어쓰기도 포함)으로 open한다는 의미
    ㄴ encoding = "utf8" 을 안하면 한글이 이상하게 출력되는 경우가 있어서 이왕이면 작성 해 두자.
score_file.close()
    ㄴ 연 파일은 반드시 닫아줘야 함.
'''

score_file = open("score.txt","w",encoding = "utf8")
print("수학 : 0",file=score_file) # 파일에 값 넣는 첫 번째 방법
print("영어 : 50",file=score_file)
score_file.close()

# 위를 실행 시 프린트문이 있음에도 VS 에서는 출력되지 않고 score.txt 라는 이름의 파일이 폴더에 생김을 알 수 있다.

# < score.txt > 파일에
# 수학 : 0
# 영어 : 50      열어보면 이 값들이 score.txt에 들어있음.


#-----------------------------------------------------------------------------------------------------------


score_file = open("score.txt","a",encoding = "utf8")
score_file.write("과학 : 80")  # 파일에 값 넣는 두 번째 방법
score_file.write("\n코딩 : 100")
score_file.close()

# < score.txt > 파일에
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

'''
"w" 는 덮어쓰기이고 "a"는 이미 존재하는 파일의 뒤에 이어서 쓰고 싶다는 뜻임. 어팬드.
print("수학 : 0",file=score_file) 에서 프린트문은 기본으로 실행 이루 줄바꿈이 들어가는데
score_file.write("과학 : 80") 이렇게 하면 줄바꿈이 들어가지 않으므로 \n 을 적어 준 것이다.
'''


#-----------------------------------------------------------------------------------------------------------


score_file = open("score.txt","r",encoding = "utf8")
print(score_file.read())
score_file.close()

# < VS 창에 >
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

'''
"r" 파일의 내용을 읽어오는 목적으로 파일을 읽는다는 의미.
read 함수는 파일의 모든 내용을 읽어 와서 출력한다는 의미임.
'''


#-----------------------------------------------------------------------------------------------------------


score_file = open("score.txt","r",encoding = "utf8")
print(score_file.readline()) # 한 줄 읽고 커서는 다음 줄로 이동됨.
print(score_file.readline()) # 한 줄 읽고 커서는 다음 줄로 이동됨.
print(score_file.readline()) # 한 줄 읽고 커서는 다음 줄로 이동됨.
print(score_file.readline()) # 한 줄 읽고 커서는 다음 줄로 이동됨.
score_file.close()

# < VS 창에 >
#수학 : 0

#영어 : 50

#과학 : 80

#코딩 : 100

# 만약 줄바꿈을 안하고 싶다면?

score_file = open("score.txt","r",encoding = "utf8")
print(score_file.readline(),end = "") # 한 줄 읽고 커서는 다음 줄로 이동됨.
print(score_file.readline(),end = "") # 한 줄 읽고 커서는 다음 줄로 이동됨.
print(score_file.readline(),end = "") # 한 줄 읽고 커서는 다음 줄로 이동됨.
print(score_file.readline()) # 한 줄 읽고 커서는 다음 줄로 이동됨.
score_file.close()

# < VS 창에 >
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100


#-----------------------------------------------------------------------------------------------------------


# 현재 해당 파일에 몇줄이 있는지 아므로 4번 출력한 건데, 다른사람의 파일 등의 사유로 총 몇줄인지 모를 때는??

score_file = open("score.txt","r",encoding = "utf8")
while True: # 무한루프
    line = score_file.readline()
    if not line: # 만약 라인에 내용이 없다면
        break # 무한루프 종료
    print(line,end="") # 줄바꿈 없이 출력할 때
score_file.close()

# < VS 창에 >
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

#-----------------------------------------------------------------------------------------------------------


# 리스트에 값을 다 넣어 처리하고자 한다면??

score_file = open("score.txt","r",encoding = "utf8")
lines = score_file.readlines() # 모든 라인을 가져와 lines라는 이름의 리스트에 저장을 함
for i in lines:
    print(i,end="")
score_file.close()

# < VS 창에 >
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100