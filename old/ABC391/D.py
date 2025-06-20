# use longlong if translate into C++

N, W = list(map(int, input().split()))
blocks = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
queries = []
for i in range(Q):
    T, A = list(map(int, input().split()))
    queries.append([T, A-1, i])
queries.sort()

# print(queries)

ans = [None]*Q

stacks = [[] for _ in range(W)]
for i, (x, y) in enumerate(blocks):
    stacks[x-1].append((y, i))

for w in range(W):
    stacks[w].sort(reverse=True)

exists = [1]*N
w = 0
bottoms = []
idxs = [len(stacks[w])-1 for w in range(W)]
for t, a, i in queries:
    while idxs[w] >= 0 and stacks[w][idxs[w]][0] <= t:
        bottoms.append(stacks[w][idxs[w]][1])
        idxs[w] -= 1
        w += 1
        if w == W:
            for p in bottoms:
                exists[p] = 0
            w = 0
            bottoms = []
    
    ans[i] = 'Yes' if exists[a] else 'No'

print(*ans, sep='\n')

