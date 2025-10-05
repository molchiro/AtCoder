N, M, Y = list(map(int, input().split()))
A = list(map(int, input().split()))

# ちょうどM種類のセミが大量発生している最初の年をリストアップ
ans = 0
tairyo = set()
from itertools import combinations
from math import lcm
for pattern in combinations(range(N), M):
    # 選んだM種の最小こうばいすう
    pattern_A = []
    for p in pattern:
        pattern_A.append(A[p])
    k = lcm(*pattern_A)
    # 他のセミが大量発生していないか
    for i in range(N):
        if i in pattern:
            continue

        if k%A[i] == 0:
            ans -= Y//k
            # print(pattern, ans)
            break
    else:
        ans += Y//k
    
    print(pattern, ans)


print(ans)