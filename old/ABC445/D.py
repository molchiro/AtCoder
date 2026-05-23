H, W, N = list(map(int, input().split()))
chocos_H = []
chocos_W = []
for i in range(N):
    h, w = list(map(int, input().split()))
    chocos_H.append((i, h, w))
    chocos_W.append((i, h, w))
    
chocos_H.sort(key=lambda x: x[1])
chocos_W.sort(key=lambda x: x[2])

# print(chocos_H)
# print(chocos_W)

f = 1
ct = 0
seen = [0]*N
ans = [None]*N
now_h = 1
now_w = 1
while ct < N:
    if f:
        while seen[chocos_H[-1][0]]:
            chocos_H.pop()

        if chocos_H[-1][1] != H:
            f = 0
            continue

        i, h, w = chocos_H.pop()
        seen[i] = 1
        ans[i] = (now_h, now_w)
        now_w += w
        W -= w
    else:
        while seen[chocos_W[-1][0]]:
            chocos_W.pop()
    
        if chocos_W[-1][2] != W:
            f = 1
            continue

        i, h, w = chocos_W.pop()
        seen[i] = 1
        ans[i] = (now_h, now_w)
        now_h += h
        H -= h

    ct += 1

for i in range(N):
    print(*ans[i])