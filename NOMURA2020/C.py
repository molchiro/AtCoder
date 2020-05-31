N = int(input())
A = list(map(int, input().split()))
cap = [[0, 0] for _ in range(N+1)]
cap[-1] = [A[-1], A[-1]]
for i in range(N-1,-1,-1):
    cap[i][0] = (cap[i+1][0] + 2 - 1)//2
    cap[i][1] = cap[i+1][1] + A[i]
ans = 1
nodes = 1
failed = nodes < cap[0][0]
for i in range(N):
    nodes = min((nodes - A[i])*2, cap[i+1][1])
    if nodes < cap[i+1][0]:
        failed = True
        break
    ans += nodes
print(-1 if failed else ans)
