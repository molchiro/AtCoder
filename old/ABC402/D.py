N, M = list(map(int, input().split()))
lines = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
lines.sort()

d = [[] for _ in range(N)]
for u, v in lines:
    d[u].append(v)
for i in range(N):
    d[i].sort()
print(d)


imos = [0]*N
for u, v in lines:
    imos[u] += 1
    imos[v] -= 1

for i in range(1, N):
    imos[i] += imos[i-1]

print(imos)

# from bisect import bisect_left, bisect_right

ans = 0
# for u, v in lines:
