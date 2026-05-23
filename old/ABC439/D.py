N = int(input())
A = list(map(int, input().split()))
Ai = [x//7 if x%7==0 else 0 for x in A]
Aj = [x//5 if x%5==0 else 0 for x in A]
Ak = [x//3 if x%3==0 else 0 for x in A]

# print(Ai)
# print(Aj)
# print(Ak)

from collections import defaultdict

# print(cumsum_i)
# print(cumsum_k)


ans = 0

accum_i = defaultdict(int)
accum_k = defaultdict(int)
for j in range(N):
    accum_i[Ai[j]] += 1
    accum_k[Ak[j]] += 1

    n = Aj[j]
    if n == 0:
        continue

    ans += accum_i[n]*accum_k[n]

accum_i = defaultdict(int)
accum_k = defaultdict(int)
for j in range(N-1, -1, -1):
    accum_i[Ai[j]] += 1
    accum_k[Ak[j]] += 1

    n = Aj[j]
    if n == 0:
        continue

    ans += accum_i[n]*accum_k[n]

    
print(ans)
