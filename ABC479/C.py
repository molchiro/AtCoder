N, W = list(map(int, input().split()))
# print(N)
okazu = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for pattern in range(1 << N):
    w = 0
    o = 0
    for i in range(N):
        if pattern >> i & 1:
            o += okazu[i][0]
            w += okazu[i][1]
    if w <= W:
       ans = max(ans, o)

print(ans) 