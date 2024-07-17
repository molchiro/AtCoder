from functools import cache
import sys

sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

ans = [0]*N

def dfs(u, seen: set, stack: list):
    global ans, A



    if u in seen:
        # found loop
        idx = stack.index(u)
        # (idx)
        l = len(stack)
        for i in range(l):
            v = stack[i]
            ans[v] = l-min(i, idx)
        return
    
    seen.add(u)
    stack.append(u)
    if ans[A[u]] != 0:
        while stack:
            v = stack.pop()
            ans[v] = ans[A[v]] + 1
            u = A[v]
    else:
        dfs(A[u], seen, stack)
        
for i in range(N):
    if ans[i] == 0:
        seen = set()
        stack = []
        dfs(i, seen, stack)
print(sum(ans))