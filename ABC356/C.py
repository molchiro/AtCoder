N, M, K = list(map(int, input().split()))

from itertools import combinations
patterns = []
for i in range(N+1):
    patterns += [set(p) for p in combinations(range(N), i)]
f = [1]*len(patterns)

# print(list(patterns))

for _ in range(M):
    S = input().split()
    C = int(S[0])
    A = set(map(lambda x: int(x) - 1, S[1:1+C]))
    R = S[-1]
    # print(C, A, R)
    if R == 'o':
        for i, p in enumerate(patterns):
            if len(p & A) < K:
                f[i] = 0
    else:
        for i, p in enumerate(patterns):
            if len(p & A) >= K:
                f[i] = 0
    
print(sum(f))

