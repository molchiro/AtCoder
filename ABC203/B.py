N, K = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(K):
        ans += 100*(i+1)+(j+1)
print(ans)