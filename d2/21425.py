# 테스트 케이스의 수 T
t = int(input())

# A, B, N
for i in range(t):
    count = 0
    a, b, n = map(int, input().split())
    x, y = a, b
    ma = max(x, y)
    mi = min(x, y)
    while ma <= n:
        mi += ma
        ma = max(mi, ma)
        mi = min(mi, ma)
        count += 1

    print(count)


