N, M = list(map(int, input().split()))
actions = [list(map(int, input().split())) for _ in range(M)]
actions.sort(key=lambda x: x[1])

ans = 0
tmp = N-1
for A, C in actions:
    A %= tmp
    if A == 0:
        continue
    ans += C * (tmp-tmp%A)
    tmp %= A
    tmp += 1
    if tmp == 1:
        print(ans)
        exit()

print(-1)