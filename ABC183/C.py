from itertools import permutations

N, K = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for route in permutations(range(N), N):
    total = 0
    s = route[0]
    now = 0
    for to in route:
        total += T[now][to]
        now = to
    total += T[now][s]
    if total == K:
        ans += 1
print(ans)