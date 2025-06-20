N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(list)

for i, a in enumerate(A):
    dd[a].append(i)

left = -1

array = []

from bisect import bisect_left, bisect_right

for b in B:
    if len(dd[b]) == 0:
        print('No')
        exit()
    
    # leftより右の中で一番左の要素を選ぶ
    idx = bisect_right(dd[b], left)
    # leftより右に要素がなければ失敗
    if idx == len(dd[b]):
        print('No')
        exit()

    # print(left, dd[b], idx)

    left = dd[b][idx]
    array.append(left)

# print(dd)
# print(array)

prev = N
# 右から順に調べて、要素を右にずらせるものが１つでもあればクリア
for i in range(M-1, -1, -1):
    b = B[i]
    idx = array.pop()

    # print(i, b, idx, dd[b])

    while dd[b][-1] > prev:
        dd[b].pop()
    r = dd[b].pop()

    if idx < r:
        print('Yes')
        break

    prev = idx


else:
    print('No')