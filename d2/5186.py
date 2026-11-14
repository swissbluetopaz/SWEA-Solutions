T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = float(input())
    x = N
    num = 12
    s = ""
    while num > 0:
        # 정수부 k
        k = int(2 * x)
        num -= 1
        s += str(k)
        x = 2 * x - k
        if x == 0:
            print(f"#{test_case} {s}")
            break
    if x != 0:
        print(f"#{test_case} overflow")