
# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.
# 제공하는 클래스는 매우 다양하지만, 코딩테스트에서 가장 유용하게 사용할 수 있는 클래스는
# permutations, combinations이다.
# permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
# permutations는 크래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
# 리스트['A', 'B', 'C']에서 3개(r=3)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.
from itertools import permutations

data = ['A','B','C'] #데이터 준비
result = list(permutations(data,2)) #모든 경우의 수(순열) 구하기
print(result)

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다. 리스트['A', 'B', 'C']에서 2개(r=2)를 뽑아
#  순서에 상관없이 나열하는 모든 경우를 출력하는 예시는 다음과 같다.

from itertools import combinations
data =['A','B','C'] #데이터 준비
result = list(combinations(data,2)) #2개를 뽑는 모든 조합 구하기
print(result)

# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬
# 로 나열하는 모든 경우(순열)를 계산한다. 다만 원소를 중복하여 뽑는다. product 객체를 초기화 할 때는
# 뽑고자 하는 데이터의 수를 repeat속성값으로 넣어준다. product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
# 리스트  ['A','B','C']에서 중복을 포함하여 2개(r=2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.
from itertools import product
data =  ['A','B','C'] #데이터 준비
result = list(product(data,repeat=2))
print(result)

# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고
# 나열하는 모든 경우(조합)를 계산한다. 다만 원소를 중복해서 뽑는다. combinations_with_replacement는 클래스이므로 객체 초기화 이후에는
# 리스트 자료형으로 변환하여 사용해야 한다. 리스트 ['A','B','C']에서 중복을 포함하여 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든
# 경우를 출력하는 예시는 다음과 같다.

from itertools import combinations_with_replacement

data = ['A','B','C'] #데이터 준비
result = list(combinations_with_replacement(data,2))
print(result)

