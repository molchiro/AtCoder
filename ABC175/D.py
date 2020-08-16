N, K = list(map(int, input().split()))
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))
ans = -10**9-1
for i in range(N):
    cumsum = [0]*(N+1)
    seen = [-1]*N
    K_ = K
    now = i
    j = 0
    while K_ > 0 and seen[now] == -1:
        seen[now] = 1
        now = P[now]
        cumsum[j+1] = cumsum[j] + C[now]
        K_ -= 1
        j += 1
    if K_ == 0:
        ans = max(ans, max(cumsum[1:j+1]))
    else:
        if cumsum[j] > 0:
            loop_size = j
            loop_n = K//loop_size - 1
            K_ %= loop_size
            tmp = loop_n*cumsum[loop_size]
            tmp += max(max(cumsum[1:loop_size+1]), cumsum[loop_size] + max(cumsum[0:K_+1]))
            ans = max(ans, tmp)
        else:
            ans = max(ans, max(cumsum[1:j+1]))
print(ans)