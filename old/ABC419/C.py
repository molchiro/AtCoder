N = int(input())
peaple = [list(map(int, input().split())) for _ in range(N)]

center = [int(sum([x for x, y in peaple])/N), int(sum([y for x, y in peaple])/N)]
# center = [sum([x for x, y in peaple])/N, sum([y for x, y in peaple])/N]
# print(center)

ans = 10**18
for dr in range(-10, 10):
    for dc in range(-10, 10):
        cr = center[0] + dr
        cc = center[1] + dc

        # print(cr, cc)

        tmp = 0
        for r, c in peaple:
            d = max(abs(cr-r), abs(cc-c))
            # print(d)
            tmp = max(tmp, d)
        ans = min(ans, tmp)





print(ans)