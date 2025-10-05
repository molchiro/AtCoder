Q = int(input())
nxt = dict()
prv = dict()

for i in range(Q):
    t, *rem = list(map(int, input().split()))
    if t == 1:
        x = rem[0]
        if x in nxt:
            prv[nxt[x]] = i+1
            prv[i+1] = x
            nxt[i+1] = nxt[x]
            nxt[x] = i+1
        else:
            nxt[x] = i+1
            prv[i+1] = x

    else:
        x, y = rem
        # どっちが左側かチェック
        l = x
        r = x
        while True:
            if l not in prv:
                break
            elif r not in nxt:
                x, y = y, x
                break
            elif prv[l] == y:
                x, y = y, x
                break
            elif nxt[r] == y:
                break
            
            l = prv[l]
            r = nxt[r]

        ans = 0
        while nxt[x] != y:
            ans += nxt[x]
            prv[nxt[nxt[x]]] = x
            prv.pop(nxt[x])
            nxt[x] = nxt.pop(nxt[x])

        print(ans)

    # print(nxt, prv)