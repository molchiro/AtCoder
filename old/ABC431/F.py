import sys
sys.setrecursionlimit(10**6)

from atcoder.modint import Modint, ModContext
from functools import cache
from bisect import bisect_left, bisect_right
from collections import Counter

mod = 998244353
with ModContext(mod):

    # 下準備
    kaijo = [Modint(1)]
    for i in range(1, 2*(10**5)+10):
        kaijo.append((kaijo[-1]*Modint(i)))

    # 前処理
    N, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    print(A)
    # print([A[i+1] - A[i] for i in range(N-1)])

    # Aのrまでの要素が取りうるパターンの数
    @cache
    def solve(r):
        global A, D, N
        if r == 0:
            return Modint(1)
        # 右端がどこまで左に行けるか二分探索
        l = bisect_right(A, A[r]-D)
        # r番目の要素をl -> r まで移動させた時の
        res = Modint(1)
        for i in range(l, r+1):
            res += solve(i) * culc(i, r+1)
        return res
    
    @cache
    def culc(lr):
        global A, D, N
        l, r = lr
        B = A[l:r]
        C = Counter(B)
        res = kaijo(len(B))
        for v in C.values():
            res *= kaijo[v].inv()

    print(solve(N-1).val())
