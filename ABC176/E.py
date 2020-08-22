H, W, M = list(map(int, input().split()))

targets = set()
row = [0]*H
col = [0]*W

for _ in range(M):
    h, w = list(map(lambda x: int(x) - 1, input().split()))
    row[h] += 1
    col[w] += 1
    targets.add((h, w))

r_max = max(row)
c_max = max(col)
ans = 0
# print([h for h in range(H) if row[h] == r_max])
# print([w for w in range(W) if col[w] == c_max])
for h in [h for h in range(H) if row[h] == r_max]:
    for w in [w for w in range(W) if col[w] == c_max]:
        # print(r_max + c_max - 1 if (h, w) in targets else 0)
        ans = max(ans, r_max + c_max - (1 if (h, w) in targets else 0))
print(ans)

