N = int(input())
S = input()
T = input()

from collections import defaultdict
place = defaultdict(list)
for i, s in enumerate(S):
    place[s].append(i)

from bisect import bisect_left

def check(K):
    global S, T, N
    global place
    now = -1
    n = 1 # tをそれぞれK個揃えるのに必要なSの個数を数える
    for t in T:
        k = K
        p = place[t]
        print(K, t, p, n, now)

        # tが存在しないならば失敗
        if p == []:
            return False

        # 余りからtをいくつとれるか計算
        idx = bisect_left(p, now+1)
        l = len(p)-idx

        # 余りだけで足りた場合
        if l >= k:
            now = p[k-1]
            continue

        k -= l

        # Sに含まれるtをlen(p)個rセット分全て取り、さらにq個消費する
        r, q = divmod(k, len(p))
        n += r
        now = p[q-1]
        if q:
            n += 1
        print(l, r, q)
        if n > N:
            return False
        
    return True

ok = 0
ng = (len(S)*N+len(T)-1)//len(T) + 1
while ng - ok > 1:
    m = (ok+ng)//2
    if check(m):
        ok = m
    else:
        ng = m

print(ok)