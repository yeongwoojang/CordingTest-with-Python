# input() : 한 줄의 문자열을 입력 받도록 해준다.

# 입력을 위한 전형적인 소스코드
# 데이터 개수 입력
n = int(input())
#각 데이터를 공백으로 구분하여 입력
# input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤에,
# map을 이용하여 해당 리스트의 모든 원소에 int() 함수를 적용한다.
# 최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저정하게 된다.
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int,input().split())

print(n,m,k)

# 입력을 최대한 빠르게 받아야 하는 경우.
# 흔히 정렬, 이진 탐색, 최단 경로 문제의 경우
# 매우 많은 수의 데이터가 연속적으로 입력이 되곤 한다. 예를들어 1000만개가 넘는
# 라인이 입력되는 경우, 입력을 받는 것만으로도 시간 초과를 받을 수 있다.
# input()함수는 동작 속도가 느려서 시간 초과가 발생할 수가 있다.
# 이경우 파이썬의 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용한다.
# sys 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 rstrip() 함수를 꼭 호출해야 한다.
# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야한다.

import sys
data = sys.stdin.readline().rstrip()
print(data)

# 출력 시 오류가 발생하는 경우
# answer = 7
# print("정답은"+7+"입니다.")
# TypeError : can only concatenate str (not "int") to str
# --> 문자열 자료형끼리만 더하기 연산이 가능하다.

answer = 7
print("정답은"+str(answer)+"입니다.")

# 각 변수를 콤마(,)로 구분하여 출력하는 경우
# 각 변수를 콤마로 구분하여 출력하는 경우, 변수의 값 사이에 의도치 않은 공백이 삽입될 수 있다.
answer = 7
print("정답은", str(answer), "입니다.")
print("asd","ASda","Adas")

# Python3.6 이상의 버전부터 f-string 문법을 사용할 수 있다.
# f-string은 문자열 앞에 접두사 'f'를 붙임으로써 사용할 수 있는데, f-string을 이용하면 단순히 중괄호 안에
# 변수를 넣음으로써 자료형의 변환 없이도 바꾸지 않고 간단히 문자열과 정수를 함께 넣을 수 있다.
answer = 7
print(f"정답은 {answer} 입니다")
