N, M = list(map(int, input().split()))
X = list(map(lambda x: int(x) - 1, input().split()))
ans = 0
imos = [0]*(N)
now = X[0]
for x in X[1:]:
    l = now
    r = x
    if l > r:
        l, r = r, l
    if r - l > N//2:
        # print('if')
        k = N - (r-l)
        ans += k
        d = N - k*2
        imos[0] += d
        imos[l] -= d
        imos[r] += d
    else:
        # print('else')
        k = r-l
        ans += k
        d = N - k*2
        imos[l] += d
        imos[r] -= d
    now = x
    # print(ans, l, r, d, imos)

for i in range(N-1):
    imos[i+1] += imos[i]
print(ans + min(imos))
