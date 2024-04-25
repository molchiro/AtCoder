S = input()
from collections import Counter
C = Counter(S)
x, n = C.most_common(1)[0]
for i, s in enumerate(S):
    if s != x:
        print(i+1)
        break