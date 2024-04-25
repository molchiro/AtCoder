def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    if str_n == '':
        return 0
    else:
        return int(str_n[::-1])

N = int(input())

ans = ''
# print(str(base_n(N-1, 5)))
for e in str(base_n(N-1, 5)):
    ans += str([0, 2, 4, 6, 8][int(e)])
print(ans)