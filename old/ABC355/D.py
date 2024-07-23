N = int(input())
events = []
for _ in range(N):
    l, r = list(map(int, input().split()))
    events.append((l, 1))
    events.append((r+1, -1))
accum = 0
ans = 0
events.sort(key=lambda x:(x[0], x[1]))
for x, y in events:
    if y == 1:
        ans += accum
        accum += 1
    else:
        accum -= 1
print(ans)
    