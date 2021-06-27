N = int(input())
area = []
for _ in range(N):
    t, l, r = list(map(int, input().split()))
    area.append([l, r, t])

area.sort()
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        l1, r1, t1 = area[i]
        l2, r2, t2 = area[j]
        if l2 < r1:
            ans += 1
        elif l2 == r1 and t1 in [1, 3] and t2 in [1, 2]:
            ans += 1
        # print(i, j, ans)
print(ans)