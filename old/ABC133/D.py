N = int(input())
A = list(map(int, input().split()))
xi = sum([A[i]*((-1)**i) for i in range(N)])
res = []
for i in range(N):
    res.append(str(int(xi)))
    xi = (A[i] - xi/2) * 2
print(" ".join(res))