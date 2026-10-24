N, V = list(map(int, input().split()))
W = list(map(int, input().split()))
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if i+j+k+3 > V:
                continue
            tmp = W[i]+W[j]+W[k]
            ans = max(ans, tmp)

print(ans)