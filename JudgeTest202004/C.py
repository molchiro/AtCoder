import itertools

a1, a2, a3 = list(map(int, input().split()))
N = a1 + a2 + a3
perms = itertools.permutations(range(1,N+1))
ans = 0
for p in perms:
    p = list(p)
    t1 = (p[0:a1] + [10]*3)[:3]
    t2 = (p[a1:a1+a2] + [10]*3)[:3]
    t3 = (p[a1+a2:] + [10]*3)[:3]
    v1 = [t1[0], t2[0], t3[0]]
    v2 = [t1[1], t2[1], t3[1]]
    v3 = [t1[2], t2[2], t3[2]]
    isSorted = lambda l: l == sorted(l)
    if isSorted(t1) and isSorted(t2) and isSorted(t3) and isSorted(v1) and isSorted(v2) and isSorted(v3):
        ans += 1
print(ans)