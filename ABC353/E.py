import sys

sys.setrecursionlimit(10**9)


N = int(input())
S = input().split()
S_n = [len(s) for s in S]
# print(S)

from collections import defaultdict

ans = 0
def dfs(idxs: set, depth: int):
    global S, ans
    # print(idxs, depth)
    next_set = defaultdict(set)
    if depth > 0:
        ans += len(idxs)*(len(idxs)-1)//2
    for idx in idxs:
        if S_n[idx] > depth:
            next_set[S[idx][depth]].add(idx)
    # print(next_set)
    # input()
    for k, v in next_set.items():
        if len(v)>=2:
            dfs(v, depth+1)

dfs(set([i for i in range(N)]), depth=0)
print(ans)