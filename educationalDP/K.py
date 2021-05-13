N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [0]*(K+1)
for i in range(K+1):
    for a in [x for x in A if x <= i]:
        if dp[i-a] == 0:
            dp[i] = 1
            break
    
print('First' if dp[K] else 'Second')