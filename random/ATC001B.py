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
        if not self.same(a, b): self.par[a] = self.root(b)

N, Q = map(int, input().split())
UF = union_find(N)
for _ in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        UF.unite(A, B)
    else:
        print('Yes' if UF.same(A, B) else 'No')
