N = int(input())
tank = 0
queries = [list(map(int, input().split())) for _ in range(N)]
idx = 0
for t in range(queries[-1][0]+1):
    if tank:
        tank -= 1
    if idx < N and queries[idx][0] <= t:
        tank += queries[idx][1]
        idx += 1

print(tank)