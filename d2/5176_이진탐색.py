def inorder(node_num):
    global count, tree, n
    if node_num <= n:
        # 1. 왼쪽 자식 방문 (2 * i)
        inorder(2 * node_num)

        # 2. 현재 노드에 값 채우기 (오름차순)
        tree[node_num] = count
        count += 1

        # 3. 오른쪽 자식 방문 (2 * i + 1)
        inorder(2 * node_num + 1)

# 테스트 케이스의 수 T
t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    # 1번부터 N번 노드까지 다루기 위해 크기가 N + 1인 리스트 생성
    tree = [0] * (n + 1)
    count = 1

    # 중위 순회 함수 실행 (루트인 1번부터 시작)
    inorder(1)

    # 루트 노드(1번)의 값과 N/2번 노드의 값 출력
    root_val = tree[1]
    half_val = tree[n//2]

    print(f'#{test_case} {root_val} {half_val}')