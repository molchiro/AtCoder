N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# 桁数*modMの辞書を持っておく -> (2*10**5) * 10 -> 10**7以下だから間に合いそう

from collections import defaultdict

dd = [defaultdict(int) for _ in range(11)]
for a in A:
    l = len(str(a))
    dd[l][a%M] += 1

# print(dd)

ans = 0

for a in A:
    for k in range(1, 11): # yにk桁の数字を選ぶとき
        q = (a*(10**k))%M
        if q == 0:
            ans += dd[k][0]
        else:
            ans += dd[k][M-q]

print(ans)

