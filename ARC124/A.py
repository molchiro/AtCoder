N, K = list(map(int, input().split()))

# はじめ全てのaについて1~K全ての値を取れる
A = [[1]*K for _ in range(N)]
for i in range(K):
    c, k = input().split()
    k = int(k)-1
    # k番目より左(または右)はiを取れなくなる
    if c =='L':
        cannot_select_range = range(k)
    else:
        cannot_select_range = range(k+1, N)
    for j in cannot_select_range:
        A[j][i] = 0
    # k番目はiに確定する。
    A[k] = [0]*K
    A[k][i] = 1
# aが取りうる値が決まったのでA全体の組み合わせを求める
ans = 1
for i in range(N):
    ans *= sum(A[i])
    ans %= 998244353
print(ans)