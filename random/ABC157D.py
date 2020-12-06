class union_find:
    def __init__(self, N):
        # par < 0 の時はsizeを格納
        self.par = [-1 for i in range(N)]
        self.excluded = [0 for i in range(N)]
    
    def root(self, a):
        if self.par[a] < 0:
            return a
        else:
            # 経路圧縮
            self.par[a] = self.root(self.par[a])
            return self.par[a]
    
    def unite(self, a, b):
        ar = self.root(a)
        br = self.root(b)
        if ar == br:
            return
        if self.par[ar] > self.par[br]:
            ar, br = br, ar
        self.par[ar] += self.par[br]
        self.par[br] = ar
    
    def friend(self, a, b):
        self.unite(a, b)
        self.excluded[a] += 1
        self.excluded[b] += 1
    
    def block(self, a, b):
        ar = self.root(a)
        br = self.root(b)
        if ar != br:
            return
        self.excluded[a] += 1
        self.excluded[b] += 1
    
    def get_friend_sugestion_size(self, a):
        return -self.par[self.root(a)] - 1 - self.excluded[a]

N, M, K = map(int, input().split())
UF = union_find(N)
for i in range(M):
    A, B = map(int, input().split())
    UF.friend(A-1, B-1)
for i in range(K):
    A, B = map(int, input().split())
    UF.block(A-1, B-1)
print(*[UF.get_friend_sugestion_size(x) for x in range(N)])