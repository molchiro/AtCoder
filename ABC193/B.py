N = int(input())
ans = float('inf')
for _ in range(N):
    A, P, X = list(map(int, input().split()))
    if X - A > 0:
        ans = min(ans, P)
    
if ans != float('inf'):
    print(ans)
else:
    print(-1)