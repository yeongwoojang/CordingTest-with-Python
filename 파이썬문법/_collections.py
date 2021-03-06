# 파이썬의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다.
# collections 라이브러리의 기능 중에서 코딩 테스트에서 유용하게 사용되는 킄ㄹ래스는 deque와 
# Counter이다.

# 보통 파이썬에서는 deque를 사용해 큐를 구현한다. 별도로 제공하는 Queue 라이브러리가 있는데
# 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 따라서 deque를 이용해 큐를 구현해야 한다는 점을 기억하자.

# 기본 리스트 자료형은 데이터 삽입, 삭제 등의 다양한 기능을 제공한다. 리스트가 있을 때 중간에 특정한 원소를 삽입하는 것도 가능하다.
# 하지만 리스트 자료형은 append() 메서드로 데이터를 추가하거나, pop() 메서드로 데이터를 삭제할 때 '가장 뒤쪽 원소'를 기준으로
# 수행된다. 따라서 앞쪽에 있는 운소를 처리할 때에는 리스트에 포함된 데이터의 개수에 따라서 많은 시간이 소요될 수 있다.
# 리스트에서 앞쪽에 있는 원소를 삭제하거나 앞쪽에 새 원소를 삽입할 때 시간복잡도는 O(N)이다.

# 가장 앞쪽에 원소 추가 ; 리스트(O(N)), deque(O(1))
# 가장 뒤쪽에 원소 추가 ; 리스트(O(1)), deque(O(1))
# 가장 앞쪽에 있는 원소 제거 ; 리스트(O(N)), deque(O(1))
# 가장 뒤쪽에 있는 원소 제거; 리스트(O(1)), deque(O(1))

# deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이딩 등의 기능은 사용할 수 없다. 다만, 연속적
# 으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로
# 사용될 수 있다. deque는 스택이나 큐의 기능을 모두 포함한다고도 볼 수 있기 때문에 스택 혹은 큐
# 자료구조의 대용으로 사용될 수 있다.

# deque는 첫 번쨰 원소를 제거할 때 popleft()를 사용하며, 마지막 원소를 제거할 때 pop()을 사
# 용한다. 또한 첫 번쨰 인덱스에 원소 x를 삽입할 때 appendLeft(x)를 사용하며, 마지막 인덱스에
# 원소를 삽일할 떄 append(x)를 사용한다.

# 따라서 deque를 큐 자료구조로 이용할 때, 원소를 삽입할 때에는 append()를 사용하고 원소를 삭
# 제할 때에는 popleft()를 사용하면 된다. 그러면 먼저 들어온 원소가 항상 먼저 나가게 된다.(FIFO)
# 리스트 [2,3,4]의 가장 앞쪽과 뒤쪽에 원소를 삽입하는 예시는 다음과 같다.

from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) #리스트 자료형으로 변환

# 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다. 구체적으로
# 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
# 따라서 원소별 등장 횟수를 세는 기능이 필요할 때 짧은 소스코드로 이를 구현할 수 있다.
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(counter['red']) # 'red'가 등장한 횟수 출력
print(dict(counter)) #사전 자료형으로 변환
