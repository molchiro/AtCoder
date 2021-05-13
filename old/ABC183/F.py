from collections import defaultdict

class union_find:
    def __init__(self, N):
        self.par = [-1 for i in range(N)]
        self.C = [defaultdict(int) for _ in range(N)]
    
    def root(self, i):
        if self.par[i] < 0:
            return i
        else:
            # 経路圧縮
            self.par[i] = self.root(self.par[i])
            return self.par[i]
    
    def same(self, a, b):
        return self.root(a) == self.root(b)
    
    def unite(self, a, b):
        if not self.same(a, b):
            root_a = self.root(a)
            root_b = self.root(b)
            if self.par[root_a] > self.par[root_b]:
                root_a, root_b = root_b, root_a
            for key in self.C[root_b].keys():
                self.C[root_a][key] += self.C[root_b][key]
            self.par[root_a] += self.par[root_b]
            self.par[root_b] = root_a

    def define_class(self, i, c):
        self.C[i][c] += 1
    
    def query2(self, i, c):
        return self.C[self.root(i)][c]

N, Q = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))
UF = union_find(N)
for i in range(N):
    UF.define_class(i, C[i])

# print(UF.C)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1]-1, query[2]-1
        UF.unite(a, b)
    else:
        x, y = query[1]-1, query[2]-1
        print(UF.query2(x, y))