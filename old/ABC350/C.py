N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
ans = []
for i, a in enumerate(A):
    while a != i:
        A[a], A[i] = A[i], A[a]
        ans.append((i+1, a+1))
        a = A[i]

print(len(ans))
for l, r in ans:
    print(l, r)
