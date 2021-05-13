from collections import defaultdict

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
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [b - a for a, b in zip(A, B)]

UF = union_find(N)
for i in range(M):
    c, d = list(map(lambda x: int(x) - 1, input().split()))
    UF.unite(c, d)

for i in range(N):
    UF.root(i)

dd = defaultdict(int)
for i in range(N):
    dd[UF.root(i)] += C[i]

if all([x == 0 for x in dd.values()]):
    print('Yes')
else:
    print('No')