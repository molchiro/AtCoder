from sortedcontainers import SortedList

N, Q = list(map(int, input().split()))

ans = N
S = SortedList([])
for _ in range(Q):
    Ln, Rn = list(map(int, input().split()))
    if len(S) > 0:
        l = S.bisect_left((Ln, 0))
        if l > 0 and S[l-1][1] >= Ln:
            l -= 1
        # if l < len(S) and Ln > S[l][1]:
        #     print('hoge')
        #     l += 1
        r = S.bisect_left((Rn, 0))
        if r < len(S) and Rn >= S[r][0]:
            r += 1

        n = max(0, r-l)
        for _ in range(n):
            Lo, Ro = S.pop(l)
            ans += Ro-Lo+1
            Ln = min(Ln, Lo)
            Rn = max(Rn, Ro)
        # print(l, r)
    S.add((Ln, Rn))
    # print(S, Ln, Rn)
    ans -= Rn-Ln+1
    print(ans)
