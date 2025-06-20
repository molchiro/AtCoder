N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = []
for i, a in enumerate(A):
    D.append((a, 0))
for i, b in enumerate(B):
    D.append((b, 1))
for i, c in enumerate(C):
    D.append((c, 2))

D.sort()

print(D)

A_stock = []
B_stock = []
c = 0

while D:
    x, t = D.pop()
    if t == 2:
        c = x
        if len(A_stock)*len(B_stock) >= K:
            break
        else:
            K -= len(A_stock)*len(B_stock)
    elif t == 1:
        B_stock.append(x)
    else:
        A_stock.append(x)

tmp = []
for a in A_stock:
    for b in B_stock:
        tmp.append(a*b)
tmp.sort(reverse=True)
print(tmp[K-1]*x)