N, K = list(map(int, input().split()))
mod = 10**9+7

ans = 0
for i in range(K, N+2):
    ans += ((N-i+1) + (N))*i//2 - (0 + i-1)*i//2 + 1
    ans %= mod
print(ans)