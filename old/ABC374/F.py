N, K, X = list(map(int, input().split()))
T = list(map(int, input().split()))

from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from collections import defaultdict

# (i, j) i日目でj番目まで出荷済みの時の不満度の最小値
dp = defaultdict(lambda: float('inf') )
dp[(0, -1)] = 0
# (i, j) i日目でj番目まで出荷済み
hq = [(0, -1)]

def update(a, to):
    global dp, hq

    if a >= dp[to]:
        return

    dp[to] = a
    heappush(hq, to)

while hq:
    i, j =  heappop(hq)

    if j >= N-1:
        continue
    
    # 出荷しない => 次のTまで進める
    t = T[min(N-1, bisect_right(T, i))]
    if t > i:
        update(dp[(i, j)], (t, j))

    # 出荷できるものを出荷する => 不満度を確定し、X日進める
    a = dp[(i, j)]
    z = bisect_right(T, i)
    k = min(K, z-1-j)
    if k > 0:
        for l in range(k):
            j += 1
            if j >= N:
                break
            a += i-T[j]
        
        update(a, (i+X, j))


ans = float('inf')
for (i, j), a in dp.items():
    if j == N-1:
        # print(i, j, a)
        ans = min(ans, a)

# print(dp)
print(ans)
