N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
X = list(set(X))
N = len(X)
X.sort()
D = [X[i+1] - X[i] for i in range(N-1)]

# print(X)
# print(D)

edges = [(-d, i) for i, d in enumerate(D)]
edges.sort()
disconnect = set([i for _, i in edges][:M-1])

# print(disconnect)

stack = []
areas = []
for i, x in enumerate(X):
    if i in disconnect:
        stack.append(x)
        areas.append(stack)
        stack = []
    else:
        stack.append(x)

if stack:
    areas.append(stack)

# print(areas)

ans = 0
for houses in areas:
    ans += houses[-1] - houses[0]
print(ans)