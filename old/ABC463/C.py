N = int(input())
takahashis = [list(map(int, input().split())) for _ in range(N)]


from atcoder.segtree import SegTree

seg = SegTree(lambda x, y: max(x, y), 0, [h for h, _ in takahashis])

events1 = [(l, i) for i, (_, l) in enumerate(takahashis)]
events1.reverse()

Q = int(input())
T = list(map(int, input().split()))

events2 = [(t, i) for i, t in enumerate(T)]
events2.sort()
ans = [None]*Q

for t, i in events2:
    while events1 and events1[-1][0] <= t:
        
        _, j = events1.pop()
        seg.set(j, 0)
    
    ans[i] = seg.all_prod()

print(*ans, sep='\n')