N = int(input())
V = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = V[i]
        x2, y2 = V[j]
        if x1 == x2:
            continue
        if -1 <= (y2-y1)/(x2-x1) <= 1:
            ans += 1

print(ans)