N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

seen = [0]*N
def dfs(i, d):
    global seen
    global N
    
    # print(seen)
    if i == N-1:
        return d
    
    if seen[i]:
        return dfs(i+1, d)
    
    ans = d
    seen[i] = 1
    for j in range(i+1, N):
        if seen[j]:
            continue
        seen[j] = 1
        ans = max(ans, dfs(i+1, d+edges[i][j-i-1]))
        seen[j] = 0

    seen[i] = 0

    return ans

if N%2:
    ans = 0
    for i in range(N):
        seen[i] = 1
        ans = max(ans, dfs(0, 0))
        seen[i] = 0
    print(ans)
else:
    print(dfs(0,0))