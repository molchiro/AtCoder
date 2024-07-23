H, W, M = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(M)]

from collections import defaultdict
dd = defaultdict(int)
dd[0] = H*W
seen_H = [0]*H
seen_W = [0]*W
for i in range(M):
    T, A, X = query[-1-i]
    if T == 1:
        if seen_H[A-1]:
            continue
        seen_H[A-1] = 1
        dd[X] += W
        dd[0] -= W
        H -= 1
    else:
        if seen_W[A-1]:
            continue
        seen_W[A-1] = 1
        dd[X] += H
        dd[0] -= H
        W -= 1

ans = []
for k, v in list(dd.items()):
    if v > 0:
        ans.append((k, v))
ans.sort()

print(len(ans))
for k, v in ans:
    print(k, v)