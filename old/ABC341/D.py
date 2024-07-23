N, M, K = list(map(int, input().split()))

from math import lcm
m = lcm(N, M)
size = m//N + m//M - 2
r, q = divmod(K-1, size)

Ni = N
Mi = M
for _ in range(q):
    if Ni < Mi:
        Ni += N
    else:
        Mi += M

print(m*r + min(Ni, Mi))