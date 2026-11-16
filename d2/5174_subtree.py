# 테스트 케이스의 수 T
t = int(input())

def count_subtree(node):
    if node == 0:
        return 0
    # 현재 노드(1) + 왼쪽 서브트리 노드 수 + 오른쪽 서브트리 노드 수
    return 1 + count_subtree(left[node]) + count_subtree(right[node])

# 간선의 개수 E와 서브트리의 루트 N
for test_case in range(1, t + 1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    # E + 1 크기의 left, right 자식 노드 리스트
    left = [0] * (e + 2)
    right = [0] * (e + 2)

    for i in range(0, len(tree), 2):
        parent, child = tree[i], tree[i + 1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    result = count_subtree(n)
    print(f'#{test_case} {result}')
