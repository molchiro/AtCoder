N = int(input())
A = list(map(int, input().split()))
G = [-1]*N
for i, a in enumerate(A):
    if a == -1:
        now = i
    else:
        G[a-1] = i

ans = [now+1]
for _ in range(N-1):
    now = G[now]
    ans.append(now+1)

print(*ans)