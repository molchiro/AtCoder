N = int(input())
A = list(map(int, input().split()))

from itertools import permutations

for pattern in permutations(range(1, N+1)):
    for i, p in enumerate(pattern):
        if A[i] == -1:
            continue

        if A[i] != p:
            break
        
    else:
        print('Yes')
        print(*pattern)
        exit()

print('No')
        