# UFで繋がっているグループわけ
# グループごとに深さ優先探索で色わけを求める

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

for i in range(N):
    UF.root(i)


groupes = [[] for _ in range(N)]
for i in range(N):
    groupes[UF.par[i]].append(i)

ans = 0
for groupe in groupes:
    if groupe == []:
        continue
    tmp = [0]*1
    col = [-1]*N
    col[groupe[0]] = 0
    def solve(N, i, groupe, col):
        if i >= N:
            tmp[0] += 1
            return
        col_ = col[:]
        colors_around = set()
        for node in graph[i]:
            colors_around.add(col_[node])
        colors_remainder = {0, 1, 2} - colors_around
        if colors_remainder == {}:
            return False
        for c in colors_remainder:
            col_[groupe[i]] = c
            solve(N, i+1, groupe, col_)
        
    solve(len(groupe), 0, groupe, col)
    if tmp[0] == 0:
        continue
    else:
        if ans == 0:
            ans += tmp[0]
        else:
            ans *= tmp[0]

print(ans)

