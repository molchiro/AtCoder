from itertools import product
import numpy as np

N, M, X = list(map(int, input().split()))
INF = 10**5 * 12 + 1
books = np.array([list(map(int, input().split())) for i in range(N)])
ans = INF
for selection in product([0, 1], repeat=N):
    selection = np.array(selection).reshape(N, 1)
    res = (books * selection).sum(axis=0)
    if min(res[1:]) >= X:
        ans = min(ans, res[0])
print(ans if ans != INF else -1)