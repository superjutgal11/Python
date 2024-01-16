'''
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간 보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt' , '2주차.txt' , '3주차.txt', ... 와 같이 만든다.
'''

for i in range(1,51):
    with open("{0}주차.txt".format(i),"w",encoding="utf8") as study_file:
        study_file.write("- {0}주차 주간 보고 -".format(i))
        study_file.write("\n부서 : ")
        study_file.write("\n이름 : ")
        study_file.write("\n업무 요약 : ")


# 나노코딩 답변
        
for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 보고 -\n".format(i))
        report_file.write("부서 :\n")
        report_file.write("이름 :\n")
        report_file.write("업무 요약 :")