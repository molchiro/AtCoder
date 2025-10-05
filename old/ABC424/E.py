from collections import defaultdict
from heapq import heapify, heappop, heappush

T = int(input())
for _ in range(T):
    N, K, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = [2**30 * a for a in A]

    dd = defaultdict(int)
    for a in A:
        dd[a] += 1
    hq = [-a for a in set(A)]
    heapify(hq)

    while K:
        a = -heappop(hq)
        if dd[a] <= K:
            # 二等分
            if dd[a//2] == 0:
                heappush(hq, -a//2)
            dd[a//2] += dd[a] * 2

            # aはなくなる
            K -= dd.pop(a)
        else:
            # 二等分
            if dd[a//2] == 0:
                heappush(hq, -a//2)
            dd[a//2] += K * 2

            # aはまだ残る
            dd[a] -= K
            K = 0
            heappush(hq, -a)

        # print(hq)
        # print(dd)
        # print([x/(2**30) for x in hq])

    X -= 1
    # X個捨てる
    while X:
        a = -heappop(hq)
        if dd[a] <= X:
            X -= dd[a]
        else:
            X = 0
            heappush(hq, -a)
    # 先頭のキーが答え
    print(-heappop(hq)/(2**30))
    

