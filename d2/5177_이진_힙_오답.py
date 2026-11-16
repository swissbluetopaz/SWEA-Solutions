# 테스트 케이스의 수 T

t = int(input())


class Heap:

    def __init__(self, *args):

        if len(args) != 0:

            self.__A = args[0]  # 파라미터로 온 리스트

        else:

            self.__A = []

    # 힙에 원소 삽입하기

    def insert(self, x):

        i = len(self.__A)

        self.__A[i] = x

        parent = (i - 1) // 2

        while i > 0 and A[i] < A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기

    def ssum(self):

        # 마지막 노드의 인덱스 = len(self.__A) - 1

        total = 0

        last_index = len(self.__A) - 1

        parent = (last_index - 1) // 2

        while parent >= 0:
            total += parent

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