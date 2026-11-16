# 테스트 케이스의 수 T
t = int(input())


class Heap:
    def __init__(self):
        self.__A = []

    # 힙에 원소 삽입하기
    def insert(self, x):
        self.__A.append(x)
        i = len(self.__A) - 1
        parent = (i - 1) // 2
        while i > 0 and self.__A[i] < self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            i = parent
            parent = (i - 1) // 2

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    def ssum(self):
        # 마지막 노드의 인덱스 = len(self.__A) - 1
        total = 0
        last_index = len(self.__A) - 1
        parent = (last_index - 1) // 2
        while parent >= 0:
            total += self.__A[parent]
            parent = (parent - 1) // 2
        return total


for test_case in range(1, t + 1):
    # 서로 다른 자연수의 개수 n
    n = int(input())
    array = list(map(int, input().split()))
    heap = Heap()
    for element in array:
        heap.insert(element)
    s = heap.ssum()
    print(f'#{test_case} {s}')