N, K = list(map(int, input().split()))
R = list(map(int, input().split()))

ans = []
def dfs(d, current):
    global R, N, ans
    # print(d, current)
    if d == N:
        return ans.append(current)
    
    for n in range(1, R[d]+1):
        dfs(d+1, current+(n,))

dfs(0, tuple())
for a in ans:
    if sum(a)%K == 0:
        print(*a)