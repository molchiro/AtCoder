class cumsum_2d:
    def __init__(self, target: list):
        self.H = len(target)
        self.W = len(target[0])
        self.inner_cumsum = [[0]*(self.W+1) for h in range(self.H+1)]
        for h in range(1, self.H+1):
            for w in range(self.W):
                self.inner_cumsum[h][w+1] += self.inner_cumsum[h][w] + target[h-1][w]
        for h in range(self.H):
            for w in range(1, self.W+1):
                self.inner_cumsum[h+1][w] += self.inner_cumsum[h][w]
    def get(self, p1: tuple, p2: tuple):
        h1, w1 = p1
        h2, w2 = p2
        ans = 0
        ans += self.inner_cumsum[h2+1][w2+1]
        ans -= self.inner_cumsum[h1][w2+1]
        ans -= self.inner_cumsum[h2+1][w1]
        ans += self.inner_cumsum[h1][w1]
        return ans

N, K = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
# 答えでにぶたん
# 命題「中央値の最小値がx以上である」が真であるxをOKとする
thresh = int(K**2//2)+1
OK = 0
NG = 10**9+1
while NG - OK > 1:
    x = (OK+NG)//2
    A_bin = [[int(A[h][w] >= x) for w in range(N)] for h in range(N)]
    A_bin_cumsum = cumsum_2d(A_bin)
    f = 1
    for h in range(N-K+1):
        for w in range(N-K+1):
            if A_bin_cumsum.get((h, w), (h+K-1, w+K-1)) < thresh:
                f = 0
    if f:
        OK = x
    else:
        NG = x
print(OK)