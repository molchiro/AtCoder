from collections import deque

class union_find:
    def __init__(self, N):
        self.par = [i for i in range(N)]
    
    def root(self, i):
        if self.par[i] == i:
            return i
        else:
            # 経路圧縮
            self.par[i] = self.root(self.par[i])
            return self.par[i]
    
    def same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b):
        if not self.same(a, b):
            self.par[self.root(a)] = self.root(b)

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
UF = union_find(N)
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    graph[A].append(B)
    graph[B].append(A)
    UF.unite(A, B)

groupes = [[] for _ in range(N)]
for i in range(N):
    groupes[UF.root(i)].append(i)

ans = 1
for group in groupes:
    if group == []:
        continue

    bfs_order = []
    seen = [0]*N
    dq = deque()
    dq.append(group[0])
    while dq:
        v = dq.popleft()
        if seen[v]:
            continue
        bfs_order.append(v)
        seen[v] = 1
        dq.extend(graph[v])

    size = len(group)
    col = [-1]*N
    def solve(i):
        global bfs_order
        global col
        global size
        res = 0
        if i >= size:
            return 1
        now = bfs_order[i]
        colors_can_use = {0, 1, 2} - set([col[v] for v in graph[now]])
        if colors_can_use == {}:
            return 0
        for c in colors_can_use:
            col[now] = c
            res += solve(i+1)
            col[now] = -1
        return res
    col[bfs_order[0]] = 0
    ans *= solve(1)*3

print(ans)
