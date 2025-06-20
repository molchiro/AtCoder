import random
import time
start_time = time.time()
rng = random.Random(1234)

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
    
def generate_limits():
    global rng
    return rng.sample(range(1, 101), 10)

def grade(x, limits):

    for i, limit in enumerate(limits):
        if x <= limit:
            return i
    return 10


# 11段階を分ける閾値のリスト（長さ10)
def solve(limits):
    global N, M, H
    global A
    global edges

    # 根本の頂点の美しさの段階によって分けておく
    directed_edges = [[] for _ in range(11)]

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
    for i in range(10, -1, -1):
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

# 初期解を均等分の区間で出す
max_score, ans = solve([9, 18, 27, 36, 45, 54, 63, 72, 81, 90])
# 区間を自動生成して時間の許す限り試す
while time.time() - start_time < 1.8:
    limits = generate_limits()
    limits.sort()
    # print(limits)
    s, p = solve(limits)
    if s > max_score:
        # print('better!!')
        ans = p

# print(max_score)
print(*ans)