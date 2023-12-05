N, M = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))
voted = [0]*N
top = 0
ans = 0
for a in A:
    voted[a] += 1
    v = voted[a]
    if v > top:
        ans = a
        top = v
    elif v == top:
        ans = min(a, ans)
    print(ans+1)