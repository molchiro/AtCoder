N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

DP = [float("inf")]*(N+K)
DP[0] = 0

for i in range(N-1):
    for j in range(1, min(K+1, N-i)):
        DP[i+j] = min(DP[i+j], DP[i] + abs(h[i] - h[i+j]))
print(DP[N-1])