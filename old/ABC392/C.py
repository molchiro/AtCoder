N = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))
Q = list(map(lambda x: int(x) - 1, input().split()))
ans = [None]*N

for i, q in enumerate(Q):
    ans[q] = Q[P[i]]+1

print(*ans)
