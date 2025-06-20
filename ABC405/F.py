N, M = list(map(int, input().split()))
lines = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
Q = int(input())
queries = []
for i in range(Q):
    queries.append((i, list(map(lambda x: int(x) - 1, input().split()))))
ans = [None]*Q
# print(lines)
# print(queries)
queries.sort(key=lambda x: x[1][1])


d = dict()

from atcoder.segtree import SegTree

seg = SegTree(lambda x, y: x+y, 0, 2*N)

for l, r in lines:
    d[r] = l
    seg.set(l, 1)

seen = [0]*(2*N)
idx = 0
for i, (a, b) in queries:
    while idx < b and idx < 2*N:
        if not seen[idx] and idx in d:
            # print(idx)
            seg.set(d[idx], -1)
            seg.set(idx, 1)
            seen[idx] = 1
        
        idx += 1

    ans[i] = seg.prod(a, b+1)

print(*ans, sep='\n')