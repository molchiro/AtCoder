N, M = list(map(int, input().split()))
bomb = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

ans = 0
for S in range(1 << N):
    recipe = set()
    for t in range(N):
        if S & (1 << t):
            recipe.add(t)
    f = 0
    last = [0]*N
    for b in bomb:
        tmp = set(b) - recipe
        if len(tmp) == 0:
            f = 1
        elif len(tmp) == 1:
            last[list(tmp)[0]] = 1
    if f == 0:
        ans = max(ans, sum(last))    

print(ans)