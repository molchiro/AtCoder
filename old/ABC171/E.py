N = int(input())
A = list(map(int, input().split()))
A = [list(map(int, list('{:031b}'.format(x)))) for x in A]
total = []
for B in zip(*A):
    total.append(sum(B))

ans = []
for a in A:
    tmp = []
    for i in range(31):
        tmp.append(str((total[i]-a[i])%2))
    ans.append(int(''.join(tmp), 2))
print(*ans)