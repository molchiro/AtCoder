N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()
ans = 1
m = points[0][1]
for x, y in points[1:]:
    if y < m:
        ans += 1

    m = min(m, y)

print(ans)