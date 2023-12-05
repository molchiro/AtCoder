# iまでみた, j議席取った時の鞍替えさせた人数でDP
N = int(input())
_Z_ = 10**5+1
dp = [[float('inf')]*(_Z_) for _ in range(N+1)]
dp[0][0] = 0
total_z = 0
for i in range(N):
    X, Y, Z = list(map(int, input().split()))
    total_z += Z
    if X < Y:
        cost = (Y-X)//2+1
        for j in range(_Z_-Z):
            # 鞍替えさせた
            dp[i+1][j+Z] = min(dp[i+1][j+Z], dp[i][j]+cost)
            # 鞍替えさせなかった
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    else:
        for j in range(_Z_-Z):
            dp[i+1][j+Z] = min(dp[i+1][j+Z], dp[i][j])

ans = float('inf')
for x in dp[-1][total_z//2+1:]:
    ans = min(ans, x)
# print(total_z)
# print(dp[-1][:total_z+1])
print(ans)