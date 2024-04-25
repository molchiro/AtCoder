from collections import defaultdict

N, K = list(map(int, input().split()))
INF = K+1
# digit_dp: 各桁の積がkeyである数字の作り方の個数
dp = defaultdict(int)
eq_prod = 1
for f, s in  enumerate(str(N)):
    dp_next = defaultdict(int)

    # less => less
    for i in range(10):
        for j, n in dp.items():
            dp_next[min(INF, i*j)] += n
        if f > 0 and i > 0:
            dp_next[min(INF, i)] += 1

    # eq => less
    for i in range(0 if f > 0 else 1, int(s)):
        dp_next[min(INF, eq_prod*i)] += 1

    # eq => eq
    eq_prod = min(INF, eq_prod*int(s))

    dp = dp_next

ans = 0 if eq_prod > K else 1
for key, value in dp.items():
    if key != INF:
        ans += value
print(ans)