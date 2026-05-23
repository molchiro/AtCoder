N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

ans = [None]*N

for i in range(N-1, -1, -1):
    if A[i] == i:
        ans[i] = i
    else:
        ans[i] = ans[A[i]]
    
print(*[v+1 for v in ans])