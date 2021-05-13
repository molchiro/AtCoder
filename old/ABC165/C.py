from itertools import combinations_with_replacement

N, M, Q = list(map(int, input().split()))
Q_ = [list(map(int, input().split())) for i in range(Q)]
ans = 0
for A in combinations_with_replacement(range(1, M+1), N):
    ans = max(ans, sum([q[3] for q in Q_ if A[q[1] - 1] - A[q[0] - 1] == q[2]]))

print(ans)