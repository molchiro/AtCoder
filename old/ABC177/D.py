class union_find:
    def __init__(self, N):
        # 子なら親のインデックス、親ならunionのサイズを負数で格納
        self.par = [-1 for i in range(N)]
    
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
            self.par[self.root(a)] += self.par[self.root(b)]
            self.par[self.root(b)] = self.root(a)

N, M = list(map(int, input().split()))
UF = union_find(N)
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    UF.unite(A, B)
    # print(UF.par)
print(-min(UF.par))