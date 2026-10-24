N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)

cumsumcumsum = [0]
for c in cumsum[1:]:
    cumsumcumsum.append(cumsumcumsum[-1]+c)

n = [0]
for i in range(1, N+1):
    n.append(n[-1]+i)

# print(cumsum)
# print(cumsumcumsum)
# print(n)

def S(r):
    global cumsum, cumsumcumsum, n

    ok = 0
    ng = N+1
    while ng - ok > 1:
        test = (ng+ok)//2
        if n[test] <= r:
            ok = test
        else:
            ng = test

    # print(r, cumsumcumsum[ok], cumsum[r-n[ok]])

    return cumsumcumsum[ok] + cumsum[r-n[ok]]

for _ in range(Q):
    L, R = list(map(int, input().split()))
    print(S(R)-S(L-1))