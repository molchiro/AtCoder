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
    
N, Q = list(map(int, input().split()))
P = []
for _ in range(N):
    P.append([1 if x == 'B' else 0 for x in input()])
cumsum = cumsum_2d(P)
# print(cumsum.get((0, 0), (2, 2)))
# print(cumsum.get((1, 1), (2, 2)))

for _ in range(Q):
    A, B, C, D = list(map(int, input().split()))
    Ar = A//N
    Br = B//N
    A -= Ar*N
    C -= Ar*N
    B -= Br*N
    D -= Br*N
    # print(A, B, C, D)
    HW = (C//N)*(D//N)*cumsum.get((0,0), (N-1, N-1)) + (D//N)*cumsum.get((0, 0), (C%N, N-1)) + (C//N)*cumsum.get((0, 0), (N-1, D%N)) + cumsum.get((0, 0), (C%N, D%N))
    Hw = (C//N)*cumsum.get((0,0), (N-1, B-1)) + cumsum.get((0, 0), (C%N, B-1)) if B > 0 else 0
    hW = (D//N)*cumsum.get((0,0), (A-1, N-1)) + cumsum.get((0, 0), (A-1, D%N)) if A > 0 else 0
    hw = cumsum.get((0, 0), (A-1, B-1)) if B > 0 and A > 0 else 0
    # print(HW, Hw, hW, hw)
    # print((C//N), cumsum.get((0,0), (N-1, B-1)), cumsum.get((0, 0), (C%N, B-1)))
    print(HW-Hw-hW+hw)