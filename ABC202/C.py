from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))

dd = defaultdict(int)
for c in C:
    dd[B[c]] += 1

ans = 0
for a in A:
    ans += dd[a]

print(ans)