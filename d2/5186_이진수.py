# 테스트 케이스의 수 T
t = int(input())

# 10진수 N
for k in range(1, t + 1):
    n = float(input())
    array = []
    for i in range(12):
        # 이진수 숫자 한 개
        a = int(n * 2)
        array.append(a)
        n = 2 * n - a
        if n == 0:
            break
    if n == 0:
        s = ''
        for element in array:
            s = s + str(element)
        print(f'#{k} {s}')
    else:
        print(f'#{k} overflow')
