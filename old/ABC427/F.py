from collections import defaultdict

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# dp[i][f] = set(): i番目まで見て直前に選んだかをfで管理した時、総和の mod M が qであるもの数

dp1 = defaultdict(int) # 直前に選んでいない
dp1[0] = 1
dp2 = defaultdict(int) # 直前に選んだ
# dp2[0] = 0
for a in A[:N//2+1]:
    ndp1 = defaultdict(int)
    ndp2 = defaultdict(int)
    for k, v in dp1.items():
        ndp1[k] += v
        ndp2[(k+a)%M] += v
    for k, v in dp2.items():
        ndp1[k] += v
    
    dp1 = ndp1
    dp2 = ndp2

dp3 = defaultdict(int) # 直前に選んでいない
dp3[0] = 1
dp4 = defaultdict(int) # 直前に選んだ
# dp4[0] = 0
for a in A[N-1:N//2:-1]:
    ndp3 = defaultdict(int)
    ndp4 = defaultdict(int)
    for k, v in dp3.items():
        ndp3[k] += v
        ndp4[(k+a)%M] += v
    for k, v in dp4.items():
        ndp3[k] += v
    
    dp3 = ndp3
    dp4 = ndp4

ans = 0

for k, v in dp1.items():
    ans += v*dp3[(M-k)%M]
    ans += v*dp4[(M-k)%M]

for k, v in dp2.items():
    ans += v*dp3[(M-k)%M]

# print(dp1)
# print(dp2)
# print(dp3)
# print(dp4)
print(ans)