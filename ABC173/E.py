mod = 1000000007
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
ans = 1
# 負になってしまう時
if A[-1] < 0 and K%2 == 1:
    for i in range(K):
        ans = ans * (A[-i-1]%mod) % mod
else:
    n = 0
    p = -1
    # Kが奇数の時は正数を奇数個、負数を偶数個取りたい
    # あらかじめ正数を一つ使っておけば、Kが偶数の場合と同様に処理できる
    if K%2 == 1:
        ans = ans * (A[p]%mod) % mod
        p -= 1
    # 正/負の候補から２つずつ消費していく
    for _ in range(K//2):
        if A[n]*A[n+1] > A[p]*A[p-1]:
            ans = ans * (A[n]%mod) % mod
            ans = ans * (A[n+1]%mod) % mod
            n += 2
        else:
            ans = ans * (A[p]%mod) % mod
            ans = ans * (A[p-1]%mod) % mod
            p -= 2        

print(ans)