from itertools import combinations
N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
# 答えでにぶたん
l = 1
r = 10**9+1
while r-l > 1:
    m = (l+r)//2
    # peopleの能力値を圧縮し、重複を弾く
    kinds = set()
    for p in people:
        kinds.add(tuple(int(x >= m) for x in p))
    f = 0
    # 条件に合う組み合わせがあるか判定
    for members in combinations(kinds, min(3, len(kinds))):
        x = (0, 0, 0, 0, 0)
        for member in members:
            x = tuple(x[i] | member[i] for i in range(5))
        if all(x):
            l = m
            break
    else:
        r = m
print(l)