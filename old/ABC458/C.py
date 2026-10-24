S = input()
N = len(S)
ans = 0
for i in range(N):
    if S[i] == 'C':
        ans += min(i, N-i-1) + 1
        # print(i, ans)
print(ans)