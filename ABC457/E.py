from atcoder.segtree import SegTree

N, M = list(map(int, input().split()))

clothes = set()
left = [[] for _ in range(N)]
right = [[] for _ in range(N)]

for _ in range(M):
    L, R = list(map(lambda x: int(x) - 1, input().split()))
    clothes.add((L, R))
    left[L].append(R)
    right[R].append(L)

for i in range(N):
    left[i].sort()
    right[i].sort()

seg = SegTree(lambda x, y: sorted(x[:]+y[:])[:2], [10**18, 10**18], [(arr[:2] + [10**18, 10**18])[:2] for arr in left]) # 左側が[l,r)のときの右端の最小値を管理
# print(left)
# print(right)

Q = int(input())


from bisect import bisect_left, bisect_right

# 2枚の布でカバーしあうパターン
# [2,3]の布と[4,5]の布で[2,5]が成立する点に注意
def judge1(s, t):
    global left, right

    if left[s] == []:
        return False
    if left[s][0] >= t:
        return False
    
    r_idx = bisect_left(left[s], t) - 1
    r = left[s][r_idx]

    if right[t] == []:
        return False
    if right[t][-1] <= s:
        return False
    
    l_idx = bisect_right(right[t], s)
    if l_idx >= len(right[t]):
        return False
    l = right[t][l_idx]

    # print((s+1, t+1), ((s+1, r+1), (l+1, t+1)))

    return l-1 <= r
    
# 1枚の布でちょうどのパターン
def judge2(s, t):
    global clothes, seg
    if not (s, t) in clothes:
        return False

    second = seg.prod(s, t+1)[1]

    return second <= t

for _ in range(Q):
    S, T = list(map(lambda x: int(x) - 1, input().split()))
    print('Yes' if judge1(S, T) or judge2(S, T) else 'No')