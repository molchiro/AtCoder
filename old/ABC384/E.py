H, W, X = list(map(int, input().split()))
P, Q = list(map(int, input().split()))
field = [[10**20]*(W+2)] + [[10**20]+ [0]*W + [10**20] for _ in range(H)] + [[10**20]*(W+2)]
for h in range(H):
    S = list(map(int, input().split()))
    for w in range(W):
        field[h+1][w+1] = S[w]

# print(*field, sep='\n')

ans = field[P][Q]

from heapq import heapify, heappop, heappush

def move(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

hq = []
seen = set()
seen.add(P*1000+Q)
for h, w in move(P, Q):
    heappush(hq, (field[h][w], h*1000+w))
    seen.add(h*1000+w)
# print(hq)
while hq:
    s, p = heappop(hq)
    if s >= ans/X:
        break
    ans += s
    for h, w in move(p//1000, p%1000):
        if h*1000+w in seen:
            continue
        heappush(hq, (field[h][w], h*1000+w))
        seen.add(h*1000+w)
    # print(ans, hq)
print(ans)