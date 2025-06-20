N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

# まずは全点の次数を調べる
rank = [len(G[i]) for i in range(N)]
print(rank)

# 2or3点の箇所は切る
now = N
for i in range(N):
    if 2 <= rank[i] <= 3:
        for v in G[i]:
            G[v].remove(i)
            G[v].append(now)
            G.append([v])
            now += 1
        G[i] = []

N = now
rank = [len(G[i]) for i in range(N)]
print(rank)

# 4点より多くある場合は一旦切ってみて上位4つを残すことにする