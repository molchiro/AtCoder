N = int(input())

g = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())

for _ in range(Q):
    t, d = list(map(int, input().split()))
    r, q = g[t-1]
    ans = d + q-d%r
    if ans < d:
        ans += r
    print(ans)