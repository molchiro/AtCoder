N, M, H = list(map(int, input().split()))
A = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]
points = [list(map(int, input().split())) for _ in range(N)]


# 専用のUF
class UnionFind:
    def __init__(self, _A) -> None:
        self.N = len(_A)
        self.par = [-a for a in _A]
    
    def root(self, u: int) -> int:
        # 負数だった場合が自分がroot
        if self.par[u] < 0:
            return u

        # 経路圧縮
        self.par[u] = self.root(self.par[u])
        return self.par[u]

    def size(self, u):
        return -self.par[self.root(u)]
    
    def is_same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)
    
    def unite(self, p: int, c: int) -> int:
        rp = self.root(p)
        rc = self.root(c)
        if rp == rc:
            return 0
        
        tmp = self.par[rc]

        self.par[rp] += tmp
        self.par[rc] = rp

        return -tmp
    
def grade(x, limits):

    for i, limit in enumerate(limits):
        if x <= limit:
            return i

    return 9


# 10段階を分ける閾値のリスト（長さ9)
def solve(limits):
    global N, M, H
    global A
    global edges

    # 根本の頂点の美しさの段階によって分けておく
    directed_edges = [[] for _ in range(10)]

    for u, v in edges:
        gu = grade(A[u], limits)
        gv = grade(A[v], limits)

        # 同じ美しさの辺は無視する
        if gu == gv:
            continue

        # 必ずvの方が美しくなるようにswap
        if gu > gv:
            u, v = v, u
            gu, gv = gv, gu
        
        directed_edges[gv].append((gu, (u, v)))
    
    # 美しい順にマージしていく
    uf = UnionFind(A)

    score = 0
    p_list = [-1]*N
    for i in range(9, -1, -1):
        # なるべく近いグレードの頂点に繋ぐ
        for _, (u, v) in sorted(directed_edges[i], reverse=True):
            # 　親が決まっていればスキップ
            if p_list[v] != -1:
                continue
            p_list[v] = u
            score += uf.unite(u, v)
        

    for i in range(N):
        if p_list[i] == -1:
            score += uf.size(i)

    return score, p_list

score, p_list = solve([10, 20, 30, 40, 50, 60, 70, 80, 90])

# print(score)
print(*p_list)