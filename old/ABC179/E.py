N, X, M = list(map(int, input().split()))
loop = []
A_set = set()
# find loop
while not X in A_set:
    loop.append(X)
    A_set.add(X)
    X = (X*X)%M

if loop[-1] == 0:
    print(sum(loop))
else:
    ans = 0

    # ループになる前の部分
    loop_L = loop.index(X)
    ans += sum(loop[0:loop_L])
    N -= loop_L

    # ループ部
    loop = loop[loop_L:]
    loop_size = len(loop)
    loop_S = sum(loop)
    ans += loop_S*(N//loop_size)

    # 端数
    ans += sum(loop[:N%loop_size])

    print(ans)