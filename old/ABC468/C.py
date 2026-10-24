N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

from itertools import permutations

ans = 0
for pattern in permutations([i+1 for i in range(N)]):
    # print(pattern)
    if P < pattern < Q:
        ans += 1

print(ans)