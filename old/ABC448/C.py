from collections import Counter

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
d = {a: i for i, a in enumerate(A)}

ct = Counter(A)

l = [[k, v] for k, v in ct.items()]
l.sort()
d = {k: i for i, (k, v) in enumerate(l)}

# print(d)

for _ in range(Q):
    K = int(input())
    B = list(map(lambda x: int(x) - 1, input().split()))
    for b in B:
        k = A[b]
        l[d[k]][1] -= 1

    for k, v in l:
        if v > 0:
            print(k)
            break

    for b in B:
        k = A[b]
        l[d[k]][1] += 1