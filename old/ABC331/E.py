N, M, L = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bads = [[] for _ in range(N)]
for _ in range(L):
    c, d = list(map(lambda x: int(x) - 1, input().split()))
    bads[c].append(d)

from sortedcontainers import SortedList
sl = SortedList([(x, i) for i, x in enumerate(B)])

ans = 0
for a, bad in zip(A, bads):
    for b_i in bad:
        sl.discard((B[b_i], b_i))
    
    if sl:
        ans = max(ans, a + sl[-1][0])

    for b_i in bad:
        sl.add((B[b_i], b_i))

print(ans)