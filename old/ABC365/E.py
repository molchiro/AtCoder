N = int(input())
A = list(map(int, input().split()))

# 累積xor
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]^a)

ans = 0
# 桁ごとに独立
for i in range(27):
    # i桁目のビットが0のものと1のもののペアの数を計算する
    ones = sum([cumsum[j]>>i&1 for j in range(N+1)])
    pairs = ones*(N+1-ones)
    for j in range(N):
        if (cumsum[j]>>i&1) ^ (cumsum[j+1]>>i&1):
            pairs -= 1
    ans += pairs*(1<<i)
print(ans)