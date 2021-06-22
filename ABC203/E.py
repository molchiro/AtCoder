from collections import defaultdict
N, M = list(map(int, input().split()))
blacks = defaultdict(set)
for _ in range(M):
    X, Y = list(map(int, input().split()))
    blacks[X].add(Y)
row_has_blacks = list(blacks.keys())
row_has_blacks.sort()
ans = {N}
for row in row_has_blacks:
    reach_from_diagonal = set()
    for Y in blacks[row]:
        if {Y-1, Y+1} & ans:
            reach_from_diagonal.add(Y)
    cant_reach = blacks[row] - reach_from_diagonal
    ans |= reach_from_diagonal
    ans -= cant_reach
    # print(ans, reach_from_diagonal, cant_reach)
print(len(ans))