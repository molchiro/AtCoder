N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
    now = 0.5
    tmp = 0
    for j in range(N):
        # print(i, j, now)
        if (i >> j) & 1:
            nxt = now + L[j]
        else:
            nxt = now - L[j]


        if now*nxt < 0:
            tmp += 1
        
        now = nxt
    
    ans = max(ans, tmp)

print(ans)