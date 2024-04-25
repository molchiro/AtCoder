N, K = list(map(int, input().split()))
S = tuple(map(int, input().split()))
D = []

def dist(u, v):
    return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5

base = 0
prev = S
for _ in range(N):
    now = list(map(int, input().split()))
    D.append(dist(prev, S) + dist(S, now) - dist(prev, now))
    base += dist(prev, now)
    prev = now
base += dist(now, S)

from atcoder.segtree import SegTree

dp = SegTree(min, float('inf'), N+1)
dp.set(0, 0)

for i in range(N):
    dp.set(i+1, dp.prod(max(0, i-K+1), i+1) + D[i])
    # print(dp.get(i+1))
# print(base)
print(base+dp.prod(max(0, N-K+1), N+1))