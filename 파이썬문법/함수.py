# def 함수명(매개변수) :
#     실행할 소스코드
#      return 반환 값

def add(a,b) :
    return a+b;

print(add(5,3))

def add2(a,b) :
    print(a+b)

add2(5,3)

def add3(a,b) :
    print(a+b);

add3(b=3, a=5);

# global키워드
# 함수 안에서 함수 밖의 변수 데이터를 변경해야하는 경우 함수에서 global키워드를 이용하면
# 해당 함수안에 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다.

a = 0

def func() :
    global a
    a+=1

for i in range(10):
    func()

print(a)

# 람다식
def add(a,b) :
    return a+b

# 일반적인 add()메서드 사용
print(add(5,3))

# 람다 표현식으로 구현한 add()메서드
print((lambda a,b : a+b)(5,3))
(lambda a,b : print(a+b))(5,3)

