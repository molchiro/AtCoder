from itertools import product

N, M = list(map(int, input().split()))
AB = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

ans = 0
for pattern in product([0, 1], repeat=K):
    dishes = [0]*N
    for i in range(K):
        dishes[CD[i][pattern[i]]] += 1
    tmp = 0
    for a, b in AB:
        if dishes[a] > 0 and dishes[b] > 0:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
