N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
back2start = [0]*(N+1)
for a in A:
    back2start[a] = 1

cont = 0
for x in back2start:
    if x:
        cont += 1
    else:
        cont = 0
    if cont >= M:
        print(-1)
        exit()

l = 0
r = 10**10
while True:
    m = (l+r)/2
    dp = [0]*(N+M+1)
    cum_sum = 0
    for i in range(N-1, -1, -1):
        cum_sum += dp[i+1]
        cum_sum -= dp[i+M+1]
        if back2start[i]:
            dp[i] = m
        else:
            dp[i] = cum_sum/M + 1
    
    if abs(dp[0] - m) < .1**3:
        break
    elif dp[0] < m:
        r = m
    else:
        l = m

print(dp[0])    