N = int(input())
A = list(map(int, input().split()))

table = [[0] for _ in range(N+1)]
for i, a in enumerate(A):
    table[a].append(i+1)
for i in range(N+1):
    table[i].append(N+1)

ans = 0
for t in table:
    ans += N*(N+1)//2
    for i in range(len(t)-1):
        x = t[i+1] - t[i] - 1
        ans -= x*(x+1)//2
print(ans)