N, K, M = list(map(int, input().split()))
stones = [list(map(int, input().split())) for _ in range(N)]
stones.sort(key=lambda x: -x[1])
m = 0
k = 0
ans = 0
seen = set()
stocks = []
for c, v in stones:
    if m < M:
        if c in seen:
            stocks.append(v)
        else:
            ans += v
            seen.add(c)
            m += 1
            k += 1
    else:
        stocks.append(v)

ans += sum(stocks[:K-k])
print(ans)