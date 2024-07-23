N = int(input())
events = [list(map(int, input().split())) for _ in range(N)]
monsters = [0]*N
actions = []
Kmin = 0
K = 0
for i in range(N):
    t, x = events[-i-1]
    if t == 1:
        if monsters[x-1] > 0:
            actions.append(1)
            monsters[x-1] -= 1
            K += 1
        else:
            actions.append(0)
    else:
        monsters[x-1] += 1
        K -=1
    Kmin = max(Kmin, -K)

if all([m == 0 for m in monsters]):
    print(Kmin)
    print(*actions[::-1], sep=' ')
else:
    print(-1)