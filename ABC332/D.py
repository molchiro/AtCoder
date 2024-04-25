from itertools import permutations


H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

def check(x, y):
    global H, W
    for h in range(H):
        for w in range(W):
            if x[h][w] != y[h][w]:
                return False
    return True

def swaped_A(R, C):
    res = []
    for r in R:
        res.append([A[r][c] for c in C])
    return res

def tentou(X):
    res = 0
    seen = set()
    for x in X:
        res += len([e for e in seen if e > x])
        seen.add(x)
    return res

ans = float('inf')
for R in permutations(range(H), H):
    for C in permutations(range(W), W):
        if check(swaped_A(R, C), B):
            ans = min(ans, tentou(R) + tentou(C))

if ans == float('inf'):
    ans = -1

print(ans)