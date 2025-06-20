N = int(input())
A = list(map(int, input().split()))

B = [[float('inf'), float('inf')] for _ in range(21)]
C = [[float('inf')]*20 for _ in range(N)]
for i in range(N-1, -1, -1):
    a = A[i]-1
    B[a].append(i)
    for j in range(20):
        C[i][j] = B[j][-2]

# print(B)
# print(*C, sep='\n')

dp = [float('inf')]*(1<<20)
dp[0] = 0
for i in range(1<<20):
    if dp[i] == float('inf'):
        continue
    for j in range(20):
        dp[i | 1<<j] = min(dp[i | 1<<j], C[dp[i]][j])

ans = 0
for i in range(1<<20):
    if dp[i] < float('inf'):
        ans = max(ans, i.bit_count())
print(ans*2)