N, M = list(map(int, input().split()))
seen = [0]*M
for _ in range(N):
    L = int(input())
    X = list(map(lambda x: int(x) - 1, input().split()))
    ans = 0
    for x in X:
        if seen[x]:
            continue
        ans = x+1
        seen[x] = 1
        break
    print(ans)
