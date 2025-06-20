N = int(input())
A = list(map(int, input().split()))

from heapq import heapify, heappop, heappush

hq = []
for i in range(N):
    # もらう
    A[i] += len(hq)

    # 0個になった人を除外
    while hq and hq[0] - i <= 0:
        heappop(hq)

    # i番目の人を追加
    heappush(hq, A[i]+i)

# 最終的な個数を計算
# print(A)

ans = [max(0, a-(N-i-1)) for i, a in enumerate(A)]
print(*ans)