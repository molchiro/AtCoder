from itertools import combinations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

f = False
for a, b, c in combinations(A, 3):
    d1 = (b[0]-a[0], b[1]-a[1])
    d2 = (c[0]-a[0], c[1]-a[1])
    if d1[0]*d2[1] - d1[1]*d2[0] == 0:
        f = True
print('Yes' if f else 'No')