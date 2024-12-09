N, Q = list(map(int, input().split()))
# 入力 を(L, (R, C))の形に加工
# 必ず１本はQ個のノードと繋がる必要があるのでこの時点で足す
ans = 0
input_list = []
for _ in range(Q):
    L, R, C = list(map(int, input().split()))
    ans += C
    if L < R:
        input_list.append((L-1, (R-1, C)))
input_list.sort()

# print(input_list)

from heapq import heapify, heappop, heappush

hq = []
idx = 0
for i in range(N-1):
    # input_listから範囲内に入ったeventを取り出す
    while idx < len(input_list) and input_list[idx][0] <= i:
        L, (R, C) = input_list[idx]
        heappush(hq, (C, R))
        idx += 1
    # 先頭が範囲外なら捨てる
    while hq and i+1 > hq[0][1]:
        heappop(hq)
    
    # 辺があれば足す、辺がなければ失敗
    if hq:
        ans += hq[0][0]
    else:
        print(-1)
        exit()

print(ans)