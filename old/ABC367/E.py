N, K = list(map(int, input().split()))
X = list(map(lambda x: int(x) - 1, input().split()))
A = list(map(int, input().split()))

doubling = [X[:]]

for i in range(100):
    pre = doubling[-1]
    doubling.append([pre[u] for u in pre])

# print(*doubling, sep='\n')

ans_idx = [i for i in range(N)]
for i in range(100):
    if K >> i & 1:
        ans_idx = [doubling[i][u] for u in ans_idx]

print(*[A[idx] for idx in ans_idx])