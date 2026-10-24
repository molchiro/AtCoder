N, M = list(map(int, input().split()))

ans = [-1]*M

for _ in range(N):
    C, S = list(map(int, input().split()))
    ans[C-1] = max(S, ans[C-1])

print(*ans)