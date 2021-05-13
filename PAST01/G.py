from itertools import combinations
from itertools import chain

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

N = int(input())
A = [[0]*N for _ in range(N)]
ans = 0
for i in range(N-1):
    A_ = list(map(int, input().split()))
    for j in range(i+1, N):
        A[i][j] = A_[j-i-1]
        A[j][i] = A_[j-i-1]
        ans += A_[j-i-1]
# two groups
for group_A in list(powerset(range(N)))[1:-1]:
    group_B = set(range(N)) - set(group_A)
    tmp = 0
    for a, b in combinations(group_A, 2):
        tmp += A[a][b]
    for a, b in combinations(group_B, 2):
        tmp += A[a][b]   
    # print(group_A, group_B)
    ans = max(ans, tmp)
# three groupes
if N > 2:
    for group_A in list(powerset(range(N)))[1:-1]:
        if N - len(group_A) < 2:
            continue
        group_B = set(range(N)) - set(group_A)
        for group_C in list(powerset(group_B))[1:-1]:
            group_D = set(group_B) - set(group_C)
            tmp = 0
            for a, b in combinations(group_A, 2):
                tmp += A[a][b]
            for a, b in combinations(group_C, 2):
                tmp += A[a][b]
            for a, b in combinations(group_D, 2):
                tmp += A[a][b] 
            # print(group_A, group_C, group_D)
            ans = max(ans, tmp)

print(ans)    