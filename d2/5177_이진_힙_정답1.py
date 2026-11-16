# 파이썬 내장 heapq 모듈을 활용한 간결하고 빠른 풀이

import heapq

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    array = list(map(int, input().split()))

    heap = []
    for x in array:
        heapq.heappush(heap, x)

    # 마지막 노드의 인덱스 : len(heap) - 1
    total = 0
    parent = (len(heap) - 2) // 2
    while parent >= 0:
        total += heap[parent]
        parent = (parent - 1) // 2

    print(f'#{test_case} {total}')

