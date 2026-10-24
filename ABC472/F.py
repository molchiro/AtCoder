N, Q = list(map(int, input().split()))
points = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    points.append((x, y))
g = (sum(x for x, y in points)/N, sum(y for x, y in points)/N)


def surface(O, A, B):
    a = (A[0] - O[0], A[1] - O[1])
    b = (B[0] - O[0], B[1] - O[1])
    # print(a, b)

    return abs(a[0]*b[1] - a[1]*b[0]) / 2

points.append(points[0])
S = [surface(g, points[i], points[i+1]) for i in range(N)]
Sg = [(S[i] * (g[0]+points[i][0] + points[i+1][0]) / 3, S[i] * (g[1]+points[i][1] + points[i+1][1]) / 3) for i in range(N)]

print(g)
print(S)
print(Sg)

cumsum_S = [0]
for s in S:
    cumsum_S.append(cumsum_S[-1] + s)

cumsum_Sg = [(0, 0)]
for sgx, sgy in Sg:
    sgx_prev, sgy_prev = cumsum_Sg[-1]
    cumsum_Sg.append((sgx_prev+sgx, sgy_prev+sgy))

print(cumsum_S)
print(cumsum_Sg)

for _ in range(Q):
    u, v = list(map(lambda x: int(x) - 1, input().split()))
    if u < v:
        s = cumsum_S[v+1] - cumsum_S[u]
        sgx = cumsum_Sg[v][0] - cumsum_Sg[u][0]
        sgy = cumsum_Sg[v][1] - cumsum_Sg[u][1]

        sd = surface(g, points[u], points[v])
        sgdx = sd * (g[0]+points[u][0] + points[v][0]) / 3
        sgdy = sd * (g[1]+points[u][1] + points[v][1]) / 3
        s -= sd
        sgx -= sgdx
        sgy -= sgdy
        print(sgx/s, sgy/s)
