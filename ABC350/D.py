N, M = list(map(int, input().split()))
from atcoder.dsu import DSU

dsu = DSU(N)
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    dsu.merge(A, B)

ans = 0
for group in dsu.groups():
    x = len(group)
    ans += x*(x-1)//2
ans -= M
print(ans)