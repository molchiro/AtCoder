# 並び替えと入れ替えを全探索

N, S, T = list(map(int, input().split()))

lines = [list(map(int, input().split())) for _ in range(N)]

from itertools import permutations

def d(ax,ay,bx,by):
    return ((bx-ax)**2 + (by-ay)**2)**0.5

ans = float('inf')
for ord in permutations(range(N)):
    for pattern in range(1<<N):
        now = (0, 0)
        tmp = 0
        for i in range(N):
            k = ord[i]
            ux, uy, vx, vy = lines[k]
            if pattern>>i & 1:
                ux, uy, vx, vy = vx, vy, ux, uy
            
            tmp += d(now[0], now[1], ux, uy)/S
            tmp += d(ux, uy, vx, vy)/T
        
            now = (vx, vy)
        ans = min(ans, tmp)

print(ans)
