N = int(input())
A = list(map(int, input().split()))
D = []
for i in range(N-1):
    D.append(A[i+1]-A[i])

# print(D)
D.append(10**18)
L = []
l = 1
for i in range(N-1):
    if D[i+1] == D[i]:
        l += 1
    else:
        L.append(l)
        l = 1
# print(L)

ans = N + (N-1)
for l in L:
    if l >= 2:
        for i in range(1, l):
            ans += i

print(ans)