#내장 함수
# 내장함수 : 펼도의 import 명령어 없이 바로 사용할 수 있는 함수
# ex) print(), input(), sum()....

# sum() : 리스트와 같은 iterable객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환.
# * iterable객체 : 반복가능한 객체(리스트, 튜플, 사전 등)
result = sum([1,2,3,4,5])
print(result)

# min() : 파라미터가 2개 이상 들어왔을 떄 가장 작은값을 반환
result = min(7,3,5,2)
print(result)

# max() : 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환
result = max(7,5,3,2)
print(result)

# eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환.
result = eval("(3+5)*7")
print(result)

# sorted() : iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다. key속성으로 정렬 기
# 준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 설정할 수 있다.

# 오름차순으로 정렬
result = sorted([9,1,8,5,4])
print(result)
# 내림차순으로 정렬
result = sorted([9,1,8,5,4],reverse=True)
print(result)

# 파이썬에서는 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다.
# 정렬 기준은 key속성을 이용해 명시할 수 있다.
result = sorted([('홍길동',35),('이순신',75),('아무개',50)],key=lambda x : x[1], reverse=True)
print(result)

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어서 굳이 sorted() 함수를
# 사용하지 않고도 sort() 함수를 사용해서 정렬할 수 있다. 이 경우 리스트 객체의 내부 값이 정렬된 값으로 바로 변경된다.
