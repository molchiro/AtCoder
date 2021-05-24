from collections import deque

H, W = list(map(int, input().split()))
field = [[0]*W for _ in range(H)]
for h in range(H):
    A = input()
    for w in range(W):
        if A[w] == '+':
            field[h][w] = 1
        else:
            field[h][w] = -1
# dp[h][w] = h, wに到達した時の先行から見た点差
dp = [[float('inf')]*(W+1) for _ in range(H+1)]
dq = deque()
dq.append((H-1, W-1))
dp[H-1][W-1] = field[H-1][W-1]
seen = [[0]*W for _ in range(H)]
while dq:
    h, w = dq.popleft()
    if seen[h][w]:
        continue
    seen[h][w] = 1
    if h > 0:
        dp[h-1][w] = min(dp[h-1][w], field[h-1][w]-dp[h][w])
        dq.append((h-1, w))
    if w > 0:
        dp[h][w-1] = min(dp[h][w-1], field[h][w-1]-dp[h][w])
        dq.append((h, w-1))
# print(*dp, sep='\n')
score = -float('inf')
if H > 1:
    score = max(score, dp[1][0])
if W > 1:
    score = max(score, dp[0][1])
if score == -float('inf'):
    print('Draw')
elif score > 0:
    print('Takahashi')
elif score < 0:
    print('Aoki')
else:
    print('Draw')