N, M = list(map(int, input().split()))
ans = ['0' for i in range(N)]
conditions = [list(map(int, input().split())) for i in range(M)]
for c in conditions:
    if N > 1 and c[0] == 1 and c[1] == 0:
        print(-1)
        break
    elif ans[c[0] - 1] == '0' or ans[c[0] - 1] == str(c[1]):
        ans[c[0] - 1] = str(c[1])
    else:
        print(-1)
        break
else:
    if N > 1 and ans[0] == '0':
        ans[0] = '1'
    print(''.join(ans))

