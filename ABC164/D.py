S = input()
dp = [int(s) for s in S[::-1]]
dp.insert(0, 0)
for i in range(len(S)):
    dp[i+1] = (dp[i+1]*pow(10, i, 2019) + dp[i])%2019

from collections import Counter

c = Counter(dp)
# print(c)
print(sum([x*(x-1)//2 for x in c.values()]))