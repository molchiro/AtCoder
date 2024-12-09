N, Q = list(map(int, input().split()))
d = {i+1: i for i in range(N)}
ans = [i+1 for i in range(N)]
for _ in range(Q):
    x = int(input())
    i_x = d[x]
    i_y = i_x + (1 if i_x < N-1 else -1)
    y = ans[i_y]
    ans[i_x] = y
    ans[i_y] = x
    d[x] = i_y
    d[y] = i_x

print(*ans)
