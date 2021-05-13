N, C = list(map(int, input().split()))
event = []
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    event.append((a, c))
    event.append((b+1, -c))
event.sort(key=lambda x: x[0])

prev_day = 0
total_cost = 0
ans = 0
for day, cost in event:
    if day != prev_day:
        ans += (day - prev_day) * min(total_cost, C)
        prev_day = day
    total_cost += cost

print(ans)