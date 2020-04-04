N = int(input())
h = list(map(int, input().split()))

DP = [0]*N
DP[1] = abs(h[0] - h[1])

for i in range(2, N):
    DP[i] = min(DP[i-1] + abs(h[i]-h[i-1]), DP[i-2] + abs(h[i]-h[i-2]))
print(DP[N-1])
