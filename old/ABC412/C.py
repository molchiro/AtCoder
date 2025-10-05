T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    now = S[0]
    s_last = S.pop()
    S = sorted(S[1:], reverse=True)
    dominos = []
    while S and now*2 < s_last:
        t = S.pop()
        if t <= now*2:
            dominos.append(t)
        else:
            break

        if S and S[-1] <= now*2:
            dominos.pop()
        else:
            now = t

    if s_last <= now*2:
        print(len(dominos)+2)
    else:
        print(-1)