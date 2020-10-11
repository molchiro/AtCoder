N = int(input())
P = list(map(int, input().split()))
seen = [False]*(200002)
ans = 0
for p in P:
    seen[p] = True
    if seen[ans]:
        while seen[ans] == True:
            ans += 1
    print(ans)