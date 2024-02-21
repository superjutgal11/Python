# 위치인수를 사용한 함수 활용
# 위치인수 = print(1,2,3) 처럼 함수에 인수를 순서대로 넣는것을 말함

def fun1(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

fun1(10,20,30,40)

a = [10,20,30,40,50]
b = 60,70,80,90,100

print(*a)
print(*b)

# 가변인수함수를 만들고 활용해 보자!
# 가변인수 = 인수를 몇개를 받는지 미정인 함수로 매개변수 앞에 애스터리스크를 붙여서 가변인수함수를 만들 수 있다.
# 가변인수의 경우 관례적으로 args라는 이름을 사용한다.


def fun3(*a):
    print(a)

# fun3([1,2,3,4,5,6]) # 여기에 *를 안붙이면 튜플형의 리스트가 출력되고


def fun4(*a):
    print(a)

# fun4(*[1,2,3,4,5,6]) # 여기에 *를 붙이니 그냥 튜플이 나오네.. 뭐지


def fun5(args):
    for arg in args:
        print(arg)

a = 10,20,30,40,504
fun5(a)


def fun10(*args):
    for i in args:
        print(i)

fun10(10,20,30,40,50)
a=[1,2,3,4,5]
fun10(*a)

# 고정인자와 가변인자를 동시에 받기
# 고정인자는 가변인자보다 반드시 앞에 위치해야 한다.
def score(name,univ,*score):
    print("학생이름:{0},출신대학:{1},".format(name,univ),end="")
    for i in score:
        print(i,end=",")
    print("")

a1,b1,*c1=input("학생 1의 이름,학교,성적을 ,로 구분하여 입력하시오.\n>").split(",")
a2,b2,*c2=input("학생 2의 이름,학교,성적을 ,로 구분하여 입력하시오.\n>").split(",")
# 여기서 input으로 값을 받을 때 고정값인 a,b는 앞에 아무것도 안썻지만 c는 가변으로 받을거라 *를 붙였다.
score(a1,b1,*c1) 
score(a2,b2,*c2)