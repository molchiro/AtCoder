N, M = list(map(int, input().split()))
imos = [0]*(N+1)

for _ in range(M):
    L, R = list(map(lambda x: int(x) - 1, input().split()))
    imos[L] += 1
    imos[R+1] -= 1

for i in range(N-1):
    imos[i+1] += imos[i]

# print(imos)
print(min(imos[:N]))