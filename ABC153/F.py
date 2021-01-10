from bisect import bisect_right
from collections import deque

N, D, A = list(map(int, input().split()))
monsters = [list(map(int, input().split())) for _ in range(N)]
monsters.sort(key=lambda x: x[0])
X_list = [x[0] for x in monsters]
ans = 0
bomb_accum = 0
vanish = deque()
for i in range(N):
    X, H = monsters[i]

    while vanish and vanish[0][0] <= X:
        bomb_accum -= vanish[0][1]
        vanish.popleft()

    n = (H-bomb_accum+A-1)//A
    if n <= 0:
        continue
    ans += n
    bomb_accum += A*n
    vanish.append((X+2*D+1, A*n))

print(ans)