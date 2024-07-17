mod = 998244353
N = int(input())
A = list(map(int, input().split()))
cumsum = [0]
dg_cumsum = [[0]*11]
for a in A:
    cumsum.append(cumsum[-1]+a)
    tmp = dg_cumsum[-1][:]
    tmp[len(str(a))] += 1
    dg_cumsum.append(tmp[:])

# print(cumsum)
# print(dg_cumsum)

ans = 0
for i in range(N-1):
    for j in range(1, 11):
        n = dg_cumsum[-1][j] - dg_cumsum[i+1][j]
        ans += A[i]*(10**j)*n
        ans %= mod
    ans += cumsum[-1] - cumsum[i+1]
    ans %= mod

print(ans)