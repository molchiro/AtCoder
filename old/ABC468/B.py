M, D = list(map(int, input().split()))
S = input()

ans = 0

for i, s in enumerate(S):
    f = 1
    for d in range(-D, D+1):
        if not 0 <= i+d < M:
            continue

        if S[i+d] == 'G':
            f = 0

    ans += f

print(ans)