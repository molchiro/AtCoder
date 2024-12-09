M = int(input())
ans = []
for i in range(10, -1, -1):
    x = 3**i
    r = M//x
    for _ in range(r):
        ans.append(i)
    M %= x
print(len(ans))
print(*ans)