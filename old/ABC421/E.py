A = list(map(int, input().split()))


from functools import cache
from collections import defaultdict
from itertools import product, combinations

def score(pattern):
    res = 0
    for a in A:
        res = max(res, a*pattern.count(a))
    return res

@cache
def solve(n, keep):
    # print(n, keep)
    m = 5-len(keep)
    # すべてのダイスをキープしているなら終了
    if m == 0:
        return score(keep)
    
    # まず残りのダイスの出目のパターンを数え上げる
    total = 0
    dd = defaultdict(int)
    for pattern in product(A, repeat=m):
        # print(pattern)
        total += 1
        dd[tuple(sorted(list(pattern)))] += 1
    
    if n == 1:  
        res = 0
        for k, v in dd.items():
            res += v/total*score(tuple(sorted(list(k)+list(keep))))
        return res

    else:
        res = 0
        for k, v in dd.items():
            # キープの仕方を全パターン試してよいものを選ぶ
            tmp = solve(n-1, keep)
            for i in range(m):
                for pattern in combinations(k, i+1):
                    tmp = max(tmp, solve(n-1, tuple(sorted(list(pattern)+list(keep)))))
            res += v/total*tmp
        return res

print(solve(3, tuple()))