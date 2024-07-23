N = int(input())
field = [[0]*(N+2)] + [[0]+ [1]*N + [0] for _ in range(N)] + [[0]*(N+2)]
P = []
for h in range(N):
    S = input()
    for w in range(N):
        s = S[w]
        if s == 'P':
            P.append((h+1, w+1))
        elif s == '#':
            field[h+1][w+1] = 0
# print(*field, sep='\n')
A, B = P
seen = [[[[0]*(N+2) for _ in range(N+2)] for _ in range(N+2)] for _ in range(N+2)]

from collections import deque
dq = deque()
dq.append((0, A, B))
while dq:
    # print(dq)
    n, a, b = dq.popleft()
    ha, wa = a
    hb, wb = b

    if seen[ha][wa][hb][wb]:
        continue

    seen[ha][wa][hb][wb] = 1

    if ha == hb and wa == wb:
        print(n)
        break

    for dh, dw in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_ha = ha
        new_wa = wa
        new_hb = hb
        new_wb = wb
        if field[ha+dh][wa+dw]:
            new_ha += dh
            new_wa += dw
        if field[hb+dh][wb+dw]:
            new_hb += dh
            new_wb += dw
        dq.append((n+1, (new_ha, new_wa), (new_hb, new_wb)))
else:
    print(-1)