H, W = list(map(int, input().split()))

ans = [['.']*W for _ in range(H)]
ans[0] = ['#']*W
ans[-1] = ['#']*W
for h in range(H):
    ans[h][0] = '#'
    ans[h][-1] = '#'

for h in range(H):
    print(''.join(ans[h]))