N = int(input())
rows = [[] for _ in range(2000)]
imos = [[0]*2001 for _ in range(2001)]
for i in range(N):
    U, D, L, R = list(map(lambda x: int(x) - 1, input().split()))
    for h in range(U, D+1):
        rows[h].append((R, i))
    imos[U][L] += 1
    imos[D+1][L] -= 1
    imos[U][R+1] -= 1
    imos[D+1][R+1] += 1

for h in range(2000):
    rows[h].append((10**18, -1))
    rows[h].sort()

for h in range(2000):
    for w in range(2000):
        imos[h+1][w] += imos[h][w]
for w in range(2000):
    for h in range(2000):
        imos[h][w+1] += imos[h][w]

# for h in range(10):
#     print(imos[h][:10])

base = 0
ans = [0]*N
for h in range(2000):
    for w in range(2000):
        if imos[h][w] == 0:
            base += 1
        elif imos[h][w] == 1:
            
            row = rows[h]
            ok = 0
            ng = len(row)-1
            while ng - ok > 1:
                test = (ng+ok)//2
                if w+1 >= row[test][0]:
                    ok = test
                else:
                    ng = test
            # print(h, w, row, row[ok])
            idx = row[ok][1]
            ans[idx] += 1
# print(ans)
for a in ans:
    print(base+a)
