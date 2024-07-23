H, W = list(map(int, input().split()))
HW = H*W
S = [input() for _ in range(H)]
S_flatten = ''.join(S)
G = [[] for _ in range(HW)]

for h in range(H):
    for w in range(W):
        u = W*h+w
        if S_flatten[u] == '#':
            continue
        # 隣接チェック
        next_of_magnet = 0
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            v = u + W*dh + dw
            if not 0 <= v < HW:
                continue
            if w == 0 and dw < 0:
                continue
            if w == W-1 and dw > 0:
                continue

            if S_flatten[v] == '#':
                next_of_magnet = 1
        
        if next_of_magnet:
            continue

        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            v = u + W*dh + dw
            if not 0 <= v < HW:
                continue
            if w == 0 and dw < 0:
                continue
            if w == W-1 and dw > 0:
                continue
            G[u].append(v)

# print(G)

ans = 0

seen = [0]*HW
from collections import deque
for i in range(HW):
    if seen[i]:
        continue
    dq = deque([i])
    next_of_magnets = []
    tmp = 0
    while dq:
        u = dq.pop()
        if seen[u]:
            continue
        tmp += 1
        seen[u] = 1
        if G[u] == []:
            next_of_magnets.append(u)
        else:
            for v in G[u]:
                dq.append(v)
    ans = max(ans, tmp)
    # print(seen)
    for u in next_of_magnets:
        seen[u] = 0
    # print(i, tmp)

print(ans)
        

