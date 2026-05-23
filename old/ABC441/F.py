N, M = list(map(int, input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
dp_prev = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    P, V = list(map(int, input().split()))

    for c in range(M):
        # 選んだ場合
        if c+P <= M:
            if dp[i+1][c+P] < dp[i][c]+V:
                dp[i+1][c+P] = dp[i][c]+V
                dp_prev[i+1][c+P] = c

        # 選ばなかった場合
        if dp[i+1][c] <= dp[i][c]:
            dp[i+1][c] = dp[i][c]
            dp_prev[i+1][c] = c

print(dp)
print(dp_prev)
Max = max(dp[-1])
print(Max)

prev_c = set([i for i in range(M+1) if dp[-1][i] == Max])
print(prev_c)
ans = []
for i in range(N, 0, -1):
    print(i)
    next_prev_c = set()
    need = 0
    not_need = 0
    for c in prev_c:

        if dp_prev[i][c] == c:
            not_need = 1
        else:
            need = 1
        next_prev_c.add(dp_prev[i][c])
    prev_c = next_prev_c
    if need and not_need:
        ans.append('B')
    elif need:
        ans.append('A')
    else:
        ans.append('C')

    print(prev_c)
print(''.join(ans[::-1]))
