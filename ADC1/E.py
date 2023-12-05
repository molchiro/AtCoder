N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [(a, 0) for a in A] + [(b, 1) for b in B]
C.sort()
ans = [[] for _ in range(2)]
for i, c in enumerate(C):
    ans[c[1]].append(i+1)
print(*ans[0])
print(*ans[1])