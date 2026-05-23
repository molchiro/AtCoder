MOD = 998244353

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

B_cumsum = [0]
for b in B:
    B_cumsum.append(B_cumsum[-1]+b)
    B_cumsum[-1] %= MOD

ans = 0

b_idx = 0
for a in A:
    while b_idx < M and B[b_idx] < a:
        b_idx += 1
    ans += a*(b_idx)
    ans -= a*(M-b_idx)
    ans += B_cumsum[-1] - B_cumsum[b_idx]
    ans -= B_cumsum[b_idx]
    ans %= MOD

    # print(ans, b_idx)

print(ans)