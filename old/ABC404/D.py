N, M = list(map(int, input().split()))
C = list(map(int, input().split()))
zoos = [[] for _ in range(N)]
for a in range(M):
    _, *zoos_ = list(map(lambda x: int(x) - 1, input().split()))
    for zoo in zoos_:
        zoos[zoo].append(a)
    

from itertools import product

ans = float('inf')
for pattern in product((0, 1, 2), repeat=N):
    # print(pattern)
    cost = 0
    animals = [0]*M
    for i, n in enumerate(pattern):
        cost += C[i]*n
        for a in zoos[i]:
            animals[a] += n
    # print(animals, cost)

    if all([a >= 2 for a in animals]):
        ans = min(ans, cost)

print(ans)