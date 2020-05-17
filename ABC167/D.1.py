N, K = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))

v = [A[:]]
now = 0
for i in range(60):
    tmp = v[-1]
    v.append([tmp[x] for x in tmp])
    if K>>i & 1:
        now = v[i][now]
print(now + 1)