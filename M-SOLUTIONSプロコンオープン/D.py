N = int(input())
nodes_cnt = [[i+1, 0] for i in range(N)]
sides = []
for i in range(N-1):
    side = list(map(int, input().split()))
    nodes_cnt[side[0]-1][1] += 1
    nodes_cnt[side[1]-1][1] += 1
    sides.append(side)
costs = list(map(int, input().split()))

nodes_cnt.sort(key=lambda x: x[1])
costs.sort()

total_res = 0
nodes_res = [0 for i in range(N)]

for i in range(N):
    n = nodes_cnt[i][0]
    cost = costs[i]
    nodes_res[n-1] = cost

    prev_len = len(sides)
    sides = [side for side in sides if not n in side]
    curr_len = len(sides)
    total_res += cost * (prev_len - curr_len)

print(total_res)
for node in nodes_res:
    print(node, end=' ')
print()
