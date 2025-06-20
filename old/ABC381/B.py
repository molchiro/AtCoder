S = input()

f = 1

for i in range(len(S)//2):
    if S[2*i] != S[2*i+1]:
        f = 0

from collections import Counter
c = Counter(S)

for k, v in c.items():
    if v not in {0, 2}:
        f = 0

print('Yes' if f else 'No')