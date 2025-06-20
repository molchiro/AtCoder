N = int(input())
A = list(map(int, input().split()))

from heapq import heappop, heappush

hq = []
offset = 0  # 遅延減少量を管理

for i in range(N):
    # A[i]をヒープサイズ分増加
    A[i] += len(hq)

    # ヒープ内の値に遅延減少量を反映
    while hq and hq[0] - offset <= 0:
        heappop(hq)

    # A[i]をヒープに追加
    heappush(hq, A[i] + offset)

    # 次の操作に向けてoffsetを増加
    offset += 1

# 結果の調整
for i in range(N):
    A[i] = max(0, A[i] - (N - i - 1))

print(*A)
