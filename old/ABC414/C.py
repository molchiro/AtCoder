A = int(input())
N = int(input())

def is_kaibun(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

# from https://pydocument.hatenablog.com/entry/2023/03/25/141259
def decimal_to_n(decimal_number, n):
    """
    decimal_numberをn進数に変換する関数
    """
    if decimal_number == 0:
        return '0'
    if n < 2 or n > 16:
        return 'nは2から16の範囲で指定してください'
    digits = '0123456789ABCDEF'
    result = ''
    while decimal_number > 0:
        digit = decimal_number % n
        result = digits[digit] + result
        decimal_number //= n
    return result



ans = 0
for i in range(1, 10**7):
    if i%10 == 0:
        continue
    rev = str(i)[::-1]

    n10 = int(rev + str(i))
    # print(n10)
    if n10 <= N:
        na = decimal_to_n(n10, A)
        # print(n10, na)
        if is_kaibun(na):
            ans += n10

    n10 = int(rev + str(i)[1:])
    # print(n10)
    if n10 <= N:
        na = decimal_to_n(n10, A)
        # print(n10, na)
        if is_kaibun(na):
            ans += n10
    
    for j in range(1, 12):
        n10 = int(rev + '0'*j + str(i))
        # print(n10)
        if n10 <= N:
            na = decimal_to_n(n10, A)
            # print(n10, na)
            if is_kaibun(na):
                ans += n10
        else:
            break

print(ans)