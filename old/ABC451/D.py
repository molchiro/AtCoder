N = int(input())

beki = [[] for _ in range(10)]

tmp = 1
while tmp < 10**9:
    s = str(tmp)
    beki[len(s)].append(s)
    tmp *= 2

stocks = [set(x) for x in beki]

for k in range(2, 10):
    for i in range(1, k):
        for s in stocks[i]:
            for t in beki[k-i]:
                stocks[k].add(s+t)


ans = []
for x in stocks:
    for e in x:
        ans.append(int(e))
ans.sort()

print(ans[N-1])
