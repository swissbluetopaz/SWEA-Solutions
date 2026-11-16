heapq란?

파이썬의 heapq는 데이터를 정렬된 상태로 유지하면서 가장 작은 값(또는 가장 큰 값)을 매우 빠르게 찾아내고
꺼낼 수 있도록 해주는 표준 라이브러리(모듈)입니다.

이진 힙(Binary Heap) 자료구조 중에서도 최소 힙(Min Heap) 기능을 파이썬 리스트 기반으로 쉽게 구현할 수 있도록 지원합니다.

heapq의 핵심 특징

1. 완전 이진 트리 기반의 구조
- 데이터가 입력될 때 완전 이진 트리 형태로 채워지며, 부모 노드의 값이 항상 자식 노드의 값보다 작거나 같은 규칙(Min Heap)
을 유지합니다.
- 따라서 트리의 맨 위(index 0)에는 항상 전체 데이터 중 가장 작은 값이 위치하게 됩니다.

2. 탁월한 시간 복잡도 (O(log N))
- 일반 리스트에 데이터를 무작위로 넣고 매번 정렬하면 O(NlogN)의 시간이 걸려 데이터가 많을 때 느려집니다.
- 반면 heapq는 원소를 추가(heappush)하거나 가장 작은 값을 꺼낼(heappop) 때 O(logN)의 시간 복잡도를 보장하므로
대량의 데이터를 다룰 때 훨씬 효율적입니다.

주요 함수 사용법

파이썬에서 heapq는 특별한 클래스를 선언하는 것이 아니라, 일반 리스트를 힙처럼 다루도록 함수에 전달하는 방식으로 사용합니다.

import heapq

# 1. 빈 리스트 생성
heap = []

# 2. 원소 추가 (heappush) - 자동으로 최소 힙 구조를 유지함
heapq.heappush(heap, 5)

heapq.heappush(heap, 3)

heapq.heappush(heap, 8)

heapq.heappush(heap, 1)

print(heap) # 출력 예 : [1, 3, 8, 5] (항상 0번 인덱스가 최솟값)

# 3. 가장 작은 원소 꺼내기(heappop)

min_val = heapq.heappop(heap)

print(min_val) # 1 (가장 작은 값이 빠져나옴)

print(heap) # [3, 5, 8] (남은 원소들로 다시 힙 구조를 정비함)

# 4. 기존 리스트를 한 번에 힙으로 변환하기 (Heapify)

my_list = [4, 1, 7, 3, 9]

heapq.heapify(my_list)

print(my_list) # [1, 3, 7, 4, 9] (O(N) 시간에 최소 힙으로 변환됨)

응용 팁 : 최대 힙(Max Heap)처럼 쓰고 싶다면?

heapq는 기본적으로 최소 힙만 지원합니다. 만약 가장 큰 값을 빠르게 꺼내고 싶다면(최대 힙),
숫자에 음수(-)를 붙여서 넣었다가 뺄 때 다시 음수를 붙여 원상복구하면 됩니다.

import heapq

nums = [4, 1, 7, 3, 9]

max_heap = []

# 넣을 때 마이너스 부호 붙이기

for n in nums:
    heapq.heappush(max_heap, -n)

# 꺼낼 때 다시 마이너스 부호 붙여서 원래 값 복원

print(-heapq.heappop(max_heap)) # 9 (가장 큰 값이 나옴)
