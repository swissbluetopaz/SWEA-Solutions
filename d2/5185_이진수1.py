# 테스트 케이스의 수 T
t = int(input())

# 자리 수 N과 N자리 16진수 X
for k in range(1, t + 1):
    n, x = input().split()
    n = int(n)
    # 2진수 4자리를 저장하기 위한 공백 문자열
    s = ''

    # 16진수 문자를 10진수 정수로 변환 후 2진수 4자리로 바꿈
    for char in x:
        char = int(char, 16)
        s += f'{char:04b}'

    print(f'#{k} {s}')

