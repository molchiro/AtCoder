N, Q = list(map(int, input().split()))
H = list(map(int, input().split()))
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

from atcoder.segtree import SegTree
from collections import defaultdict
from bisect import bisect_left, bisect_right

st = SegTree(max, 0, H)

ans = {}
queries_d = defaultdict(list)
for l, r in queries:
    queries_d[r].append(l)
stack = [-float('inf')]
for r in range(N-1, -1, -1):
    h_r = H[r]
    while -stack[-1] < h_r:
        stack.pop()

    for l in queries_d[r]:
        h_l = H[l]
        h_m = st.prod(l+1, r+1)
        k = bisect_right(stack, -h_m)

        ans[(l, r)] = k - 1


    stack.append(-h_r)
    # print(stack)

for l, r in queries:
    print(ans[(l, r)])
