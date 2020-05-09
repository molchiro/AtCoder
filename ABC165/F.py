from collections import deque
from bisect import bisect_left
import sys

sys.setrecursionlimit(10**9)
INF = 10**9 + 1

N = int(input())
A = list(map(int, input().split()))
G = [[] for i in range(N)]

for i in range(N-1):
    u, v = list(map(int, input().split()))
    G[u-1].append(v-1)
    G[v-1].append(u-1)

LIS = [INF] * N
ans = [0] * N

def dfs(v, p=-1):
    a = A[v]
    idx = bisect_left(LIS, a)
    old_val = LIS[idx]
    LIS[idx] = a

    ans[v] = bisect_left(LIS, INF)

    for u in G[v]:
        if u == p:
            continue
        dfs(u, v)
    
    LIS[idx] = old_val
    
dfs(0)

print(*ans, sep='\n')
