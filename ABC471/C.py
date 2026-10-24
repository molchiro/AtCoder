N = int(input())
A = list(map(int, input().split()))

pos = [a for a in A if a > 0]
neg = [a for a in A if a < 0]
pos.sort(reverse=True)
neg.sort()

ans = 0
now = 0

while pos or neg:
    if pos and neg:
        if pos[-1]-now < now-neg[-1]:
            nxt = pos.pop()
            ans += nxt-now
        else:
            nxt = neg.pop()
            ans += now-nxt
    elif pos:
        nxt = pos.pop()
        ans += nxt-now
    else:
        nxt = neg.pop()
        ans += now-nxt     

    now = nxt
    # print(now, ans)

print(ans)