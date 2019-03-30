import itertools

N, X = list(map(int, input().split()))
S = list(map(int, input().split()))

orders = itertools.permutations([x for x in range(N)])

ans = 0
for order in orders:
    x = X
    for selected in order:
        x = x%(S[selected])
    ans += x

print(ans%(10**9 + 7))