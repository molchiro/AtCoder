from collections import deque

T = int(input())
for _ in range(T):
    X, Y, K = list(map(int, input().split()))
    # if X == Y:
    #     print(0)
    #     continue

    # if Y%K == 0 and X > Y and X%Y == 0:
    #     ans = 0
    #     while X > Y:
    #         X //= K
    #         ans += 1
    #     print(ans)
    #     continue
    ans = 0
    while X != Y:
        if X > Y:
            X //= K
        else:
            Y //= K
        ans += 1        

    print(ans)