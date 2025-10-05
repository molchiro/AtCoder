N, M = list(map(int, input().split()))
S = input()
T = input()

imos = [0]*(N+1)

for _ in range(M):
    L, R = list(map(lambda x: int(x) - 1, input().split()))
    imos[L] += 1
    imos[R+1] -= 1

for i in range(N):
    imos[i+1] += imos[i]

ans = []
for i in range(N):
    if imos[i]%2:
        ans.append(T[i])
    else:
        ans.append(S[i])

print(''.join(ans))