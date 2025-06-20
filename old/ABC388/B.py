N, D = list(map(int, input().split()))
snakes = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, D+1):
    ans = 0
    for T, L in snakes:
        ans = max(ans, T*(L+i))
    print(ans)