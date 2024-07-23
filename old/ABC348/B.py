N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    xi, yi = P[i]
    ans = -1
    d_max = -1
    for j in range(N):
        xj, yj = P[j]
        if i == j:
            continue
        d = (xi-xj)**2 + (yi-yj)**2
        if d > d_max:
            ans = j+1
            d_max = d
    print(ans)