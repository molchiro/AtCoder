T = int(input())
for _ in range(T):
    N, W = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # x==0のとき
    tmp = 0
    for i in range(N):
        if i%(2*W) < W:
            tmp += C[i]
    ans = tmp
    # print('init', ans)
    # 1<=x<2Wのとき
    for x in range(2*W-1):
        # 抜く
        for i in range(x, N, 2*W):
            tmp -= C[i]
        # 足す
        for i in range((x+W)%(2*W), N, 2*W):
            tmp += C[i]
        ans = min(ans, tmp)
        # print(tmp)
    print(ans)
    # print('---debug')