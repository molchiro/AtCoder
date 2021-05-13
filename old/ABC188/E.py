N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
V = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
V.sort(key=lambda x: x[0])

min_cost = A[:]
max_prof = [-float('inf')]*N

for x, y in V:
    x_c = A[x]
    y_c = A[y]

    min_cost[y] = min(min_cost[x], min_cost[y])
    max_prof[y] = max(max_prof[y], y_c - min_cost[x])

print(max(max_prof))