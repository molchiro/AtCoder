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

N = int(input())
A = list(map(int, input().split()))
l = 0
r = N-1
UF = union_find(2*10**5+1)
ans = 0
while l <= r:
    if not UF.same(A[l], A[r]):
        ans += 1
        UF.unite(A[l], A[r])
    l += 1
    r -= 1
print(ans)