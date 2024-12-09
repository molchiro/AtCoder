N = int(input())
K = list(map(int, input().split()))
A = sum(K)
ans = float('inf')
for i in range(1<<N):
    B = 0
    for j in range(N):
        if i>>j & 1:
            B += K[j]
        
    ans = min(ans, max(B, A-B))
print(ans)