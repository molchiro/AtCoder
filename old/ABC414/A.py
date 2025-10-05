N, L ,R = list(map(int, input().split()))
ans = 0
for _ in range(N):
    X, Y  = list(map(int, input().split()))
    if L >= X and Y >= R:
        ans += 1
print(ans)