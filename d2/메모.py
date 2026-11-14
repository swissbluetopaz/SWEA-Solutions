T = int(input())

for test_case in (1, T + 1):
    # N은 숫자로, hex_str은 문자열 그대로 받아옵니다.
    N, hex_str = input().split()
    N = int(N)

    result = ""
    for i in range(N):
        # 16진수 글자 하나를 10진수 정수로 변환 ('A' -> 10)
        dec_num = int(hex_str[i], 16)

        # 2. 10진수를 4자리 이진수 문자열로 변환 (앞에 0 채우기 포함)
        bin_num = format(dec_num, '04b')

        # 3. 결과 문자열에 이어 붙이기
        result += bin_num

    print(f'#{test_case} {result}')
