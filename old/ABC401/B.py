N = int(input())
f = 0

ans = 0
for _ in range(N):
    S = input()

    if S == 'login':
        f = 1
    elif S == 'logout':
        f = 0
    elif S == 'private' and f == 0:
        ans += 1

print(ans)
