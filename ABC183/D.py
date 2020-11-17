N, W = list(map(int, input().split()))
users = [list(map(int, input().split())) for _ in range(N)]
imos = [0]*(2*10**5+2)

for S, T, P in users:
    imos[S] += P
    imos[T] -= P

for i in range(2*10**5+1):
    imos[i+1] += imos[i]

print('Yes' if max(imos) <= W else 'No')