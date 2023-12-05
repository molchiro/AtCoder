N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    G[A-1].append((B-1, C))
    G[B-1].append((A-1, C))

def farthest(u, d, seen):
    ans = d
    for v, c in G[u]:
        if seen[v]:
            continue
        seen[v] = 1
        ans = max(ans, farthest(v, d+c, seen))
        seen[v] = 0

    return ans


ans = 0
for i in range(N):
    seen = [0]*N
    seen[i] = 1
    ans = max(ans, farthest(i, 0, seen))

print(ans)