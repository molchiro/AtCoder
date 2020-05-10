from itertools import product
import numpy as np

N, M, X = list(map(int, input().split()))
conditions = product([0, 1], repeat=N)
A = np.array([list(map(int, input().split())) for i in range(N)])
succeed = []
for c in conditions:
    p = A * np.array(c).reshape((N, 1))
    res = p.sum(axis=0)
    if np.all(res[1:] >= X):
        succeed.append(res[0])
print(min(succeed) if len(succeed) > 0 else -1)