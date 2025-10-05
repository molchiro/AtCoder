N = int(input())
A = list(map(int, input().split()))

B = [i+1+A[i] for i in range(N)]

from collections import Counter

C = Counter(B)
# print(C)
ans = 0
for j in range(N):
    ans += C[j+1-A[j]]
print(ans)