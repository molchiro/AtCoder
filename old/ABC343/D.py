N, T = list(map(int, input().split()))
from collections import defaultdict
dd = defaultdict(int)
dd[0] = N
P = [0]*N
ans = 1

for _ in range(T):
    A, B = list(map(int, input().split()))
    now = P[A-1]
    nxt = now + B

    if dd[now] == 1:
        ans -= 1
    if dd[nxt] == 0:
        ans += 1
    
    P[A-1] = nxt
    dd[now] -= 1
    dd[nxt] += 1

    print(ans)