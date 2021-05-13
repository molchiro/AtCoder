from itertools import product
N = int(input())
if N%2:
    exit()
else:
    ans = []
    for pattern in product([-1, 1], repeat=N):
        accum = 0
        for e in pattern:
            accum += e
            if accum < 0:
                break
        else:
            if accum == 0:
                ans.append(''.join([('', '(', ')')[e] for e in pattern]))
ans.sort()
print(*ans, sep='\n')