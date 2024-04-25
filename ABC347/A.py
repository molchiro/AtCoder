N, K = list(map(int, input().split()))
A = list(map(int, input().split())) 
ans = []
for a in A:
    if a%K == 0:
        ans.append(a//K)

print(*ans)