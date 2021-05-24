from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = [0]*N
B[0] = A[0]
for i in range(1, N):
    B[i] = B[i-1]+A[i]*(-1)**i
# print(B)

d = defaultdict(int)
d[0] += 1
for b in B:
    d[b] += 1
# print(d)

ans = 0
for key in d.keys():
    n = d[key]
    ans += n*(n-1)//2
print(ans)