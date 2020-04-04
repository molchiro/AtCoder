from collections import Counter 
import itertools

N = int(input())
D = list(map(int, input().split()))
D.append(12)
M = Counter(D)
if max(M.values()) > 2:
    print(0)
elif 0 in D:
    print(0)
elif N > 11:
    print(1)
else:
    D.remove(12)
    D = [[x, 24-x] for x in D]
    generator = list(itertools.product([0, 1], repeat=N))
    D_gen = [[D[i][g[i]] for i in range(N)] for g in generator]
    ans = 0
    for d in D_gen:
        if len(set(d)) < N:
            pass
        else:
            tmp = [0] + sorted(d) + [24]
            s = 13
            for i in range(N+1):
                s = min(s, tmp[i+1]-tmp[i])
            ans = max(ans, s)
    print(ans)
