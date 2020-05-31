N, K = list(map(int, input().split()))
S = [1 if x=='R' else -1 for x in input()]
cnt = 0
rule = S[0]
f = False
for i in range(1, N):
    if S[i] != rule:
        f = True
        S[i] *= -1
    else:
        if f:
            f = False
            cnt += 1
    if cnt >= K:
        break

S.insert(0, 1)
S.append(-1)
ans = 0
for i in range(N):
    x = S[i+1]
    y = S[i+1+x]
    if x == y:
        ans += 1

print(ans)