import dataclasses

@dataclasses.dataclass
class UnionFind:
    N: int
    par: list[int] = dataclasses.field(init=False)
    chi: list[int] = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.par = [-1]*self.N
        self.chi = [-1]*self.N
    
    def root_par(self, u: int) -> int:
        # 負数だった場合が自分がroot
        if self.par[u] < 0:
            return u

        # 経路圧縮
        self.par[u] = self.root_par(self.par[u])
        return self.par[u]

    def root_chi(self, u: int) -> int:
        # 負数だった場合が自分がroot
        if self.chi[u] < 0:
            return u

        # 経路圧縮
        self.chi[u] = self.root_chi(self.chi[u])
        return self.chi[u]
    
    def merge(self, u: int, v: int) -> None:
        # par
        rpu = self.root_par(u)
        rpv = self.root_par(v)
        if rpu > rpv:
            rpu, rpv = rpv, rpu

        self.par[rpv] = rpu

        # chi
        rcu = self.root_chi(u)
        rcv = self.root_chi(v)
        if rcu > rcv:
            rcu, rcv = rcv, rcu

        self.chi[rcu] = rcv


H, W, Q = list(map(int, input().split()))

field = [[-1]*(W+2)] + [[-1]+ [1]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
uf_row = [UnionFind(W+2) for _ in range(H+2)]
uf_col = [UnionFind(H+2) for _ in range(W+2)]

def merge_cross(h, w):
    global uf_row, uf_col, field
    if field[h][w-1] == 0:
        uf_row[h].merge(w, w-1)
    if field[h][w+1] == 0:
        uf_row[h].merge(w, w+1)
    if field[h-1][w] == 0:
        uf_col[w].merge(h, h-1)
    if field[h+1][w] == 0:
        uf_col[w].merge(h, h+1)

for _ in range(Q):
    R, C = list(map(int, input().split()))

    if field[R][C]:
        field[R][C] = 0
        merge_cross(R, C)
    else:
        u = uf_col[C].root_par(R)
        d = uf_col[C].root_chi(R)
        l = uf_row[R].root_par(C)
        r = uf_row[R].root_chi(C)
        if field[R][l-1]==1:
            field[R][l-1] = 0
            merge_cross(R, l-1)
        if field[R][r+1]==1:
            field[R][r+1] = 0
            merge_cross(R, r+1)
        if field[u-1][C]==1:
            field[u-1][C] = 0
            merge_cross(u-1, C)
        if field[d+1][C]==1:
            field[d+1][C] = 0
            merge_cross(d+1, C)


ans = 0
for h in range(H):
    for w in range(W):
        ans += field[h+1][w+1]
print(ans)