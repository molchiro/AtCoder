N = int(input())
S = 'x' + input() + 'x'
ans = 0
for i in range(N):
    if S[i:i+3] == 'xxx':
        ans += 1
print(ans)