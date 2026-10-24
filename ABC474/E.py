T = int(input())
for _ in range(T):
    ans = 0

    N = int(input())
    items = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        items.append((a, b, a-b))

    items.sort(key=lambda x: (x[2], x[0]))
    m = min([a for a, _, _ in items])

    cumsum_A = [0]
    cumsum_B = [0]
    for a, b, _ in items:
        cumsum_A.append(cumsum_A[-1]+a)
        cumsum_B.append(cumsum_B[-1]+b)

    # k番目より後ろにチケット使うとする
    ans = 10**18
    for k in range(N):
        # 必要なチケット枚数
        c = N-k

        tmp = 0
        tmp += cumsum_A[k]
        tmp += cumsum_B[-1] - cumsum_B[k]
        # 足りないチケットをmで補う
        tmp += m * max(c-k, 0)

        # print(k, c, tmp)

        ans = min(ans, tmp)


    print(ans)