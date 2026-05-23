T = int(input())
for _ in range(T):
    N = int(input())
    items = [list(map(int, input().split())) for _ in range(N)]
    items.sort(key=lambda x: -x[0]-x[1])
    P = sum([p for w, p in items])
    ans = 0
    while items and P - sum(items[-1]) >= 0:
        ans += 1
        P -= sum(items.pop())
    print(ans)