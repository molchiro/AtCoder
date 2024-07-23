N, M = list(map(int, input().split()))
N += 1
ans = 0
mod = 998244353
for i in range(62):
    if M >> i & 1 == 0:
        continue

    r = 1 << (i+1)
    ans += (N//r)*(r//2)
    # print(i, ans)
    ans += max(0, N%r-r//2)
    ans %= mod
    # print(i, ans)

print(ans)