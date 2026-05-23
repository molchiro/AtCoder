def div_ceil(a, b):
    return (a+b-1)//b

from collections import Counter

T = int(input())
for _ in range(T):
    S = input()
    N = len(S)
    counter = Counter(list(S))
    items = list(counter.items())
    items.sort(key=lambda x: x[1], reverse=True)

    if items[0][1] > div_ceil(N, 2):
        print('No')
        continue

    print('Yes')
    ans = ['']*N
    i = 0
    for c, k in items:
        for _ in range(k):
            ans[i] = c
            i += 2
            if i >= N:
                i = 1
    print(''.join(ans))