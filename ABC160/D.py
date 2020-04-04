N, X, Y = list(map(int, input().split()))
neighbor = { i: [] for i in range(1, N+1) }
for i in range(1,N):
    neighbor[i].append(i+1)
    neighbor[N-i+1].append(N-i)
neighbor[X].append(Y)
neighbor[Y].append(X)

distanced_neighbor = { i: { j: [] for j in range(1, N)} for i in range(1, N+1) }
for i in range(1, N+1):
    visited = [i]
    next_nodes = neighbor[i]
    for j in range(1, N):
        distanced_neighbor[i][j] = next_nodes[:]
        queue = next_nodes[:]
        visited += next_nodes
        next_nodes = []
        for q in queue:
            for node in neighbor[q]:
                if node in visited:
                    continue
                else:
                    next_nodes.append(node)
        next_nodes = list(set(next_nodes))

for i in range(1, N):
    print(sum([len(distanced_neighbor[j][i]) for j in range(1, N+1)])//2)
    