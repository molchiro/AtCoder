N, M, Q = list(map(int, input().split()))
player = [[] for _ in range(N)]
point = [N]*M
for _ in range(Q):
    q = list(map(lambda x: int(x) - 1, input().split()))
    if q[0] == 0:
        n = q[1]
        print(sum([point[x] for x in player[n]]))
    else:
        n = q[1]
        m = q[2]
        point[m] = max(point[m] - 1, 0)
        player[n].append(m)
