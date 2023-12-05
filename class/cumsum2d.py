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