from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Ct = Counter(A)
ans = 0
for item in Ct.items():
    ans += item[0]*item[1]
for _ in range(Q):
    B, C = list(map(int, input().split()))
    B_n = Ct[B]
    ans += (C-B)*B_n
    print(ans)
    Ct[C] += Ct[B]
    Ct[B] = 0