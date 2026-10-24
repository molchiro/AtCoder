H, W, Q = list(map(int, input().split()))

f = H > W
if f:
    H, W = W, H
actions = []
for t in range(Q):
    R, C, X = input().split()
    if f:
        R, C = C, R
    actions.append((t, int(C)-1, int(R), X))
# print(actions)
actions.sort(key=lambda x: x[1])

ans = []
tmp = [(-1, 'A')]*H
for w in range(W-1, -1, -1):
    # print(actions)
    while actions and actions[-1][1] >= w:
        t, C, R, X = actions.pop()
        for r in range(R):
            if t > tmp[r][0]:
                tmp[r] = (t, X)
    # print(tmp)
    ans.append([x for _, x in tmp])


ans = ans[::-1]
ans = list(map(list, zip(*ans)))

if f:
    ans = list(map(list, zip(*ans)))

for row in ans:
    print(''.join(row))