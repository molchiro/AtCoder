N, L, R = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = []
for a in A:
    if L <= a <= R:
        ans.append(a)
    elif abs(L-a) < abs(R-a):
        ans.append(L)
    else:
        ans.append(R)
print(*ans)