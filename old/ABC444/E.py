N, D = list(map(int, input().split()))
A = list(map(int, input().split()))

# 右に要素を増やそうとしたとき、条件を満たせないことがわかったら左端から順に捨てる
# 条件の判定はsortedSet上の二分探索
from collections import deque
from sortedcontainers import SortedSet

dq = deque()
l = 0
ss = SortedSet([-10**18, 10**18])
ans = 0
for i in range(N):
    a = A[i]
    # 右端にaを挿入できるようになるまで左端を捨てる（Rが固定）
    while True:
        idx = ss.bisect_left(a)
        targets = []
        if ss[idx] == a:
            ssl = ss[idx]
            ssr = ss[idx+1]

        else:
            ssl = ss[idx-1]
            ssr = ss[idx]

        if a - ssl >= D and ssr - a >= D:
                break
        
        if a - ssl < D:
            targets.append(ssl)
        if ssr - a < D:
            targets.append(ssr)
        # print('targets', targets)
        while targets:
            e = dq.popleft()
            ss.remove(e)
            l += 1
            if e in targets:
                if e not in ss:
                    targets.remove(e)
    ss.add(a)
    dq.append(a)
    ans += i+1-l
    # print(ans, ss)
print(ans)
