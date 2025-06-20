S = input()
Q = int(input())
N = len(S)

K = list(map(int, input().split()))
for k in K:
    # print(k)
    k -= 1
    s = S[k%N]
    k //= N
    tmp = 1
    while k >= tmp:
        # k -= tmp
        tmp *= 2
    # tmp //= 2

    k += 1
    # print(k, tmp)
    f = 0
    while k > 0 and tmp > 0:
        if k > tmp:
            f = (1+f)%2
            k -= tmp
        tmp //= 2

    print(s.swapcase() if f else s, end=' ')
print()