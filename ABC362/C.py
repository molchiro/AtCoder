N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
accum = sum([r for l, r in A])
if accum < 0 :
    print('No')
    exit()

ans = []
for l, r in A:
    d = min(r-l, accum)
    ans.append(r-d)
    accum -= d

if accum != 0:
    print('No')
else:
    print('Yes')
    print(*ans)

