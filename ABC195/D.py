N, M, Q = list(map(int, input().split()))
properties = [list(map(int, input().split())) for _ in range(N)]
properties.sort(key=lambda x:x[1], reverse=True)
X = list(map(int, input().split()))
for _ in range(Q):
    L, R = list(map(lambda x: int(x) - 1, input().split()))
    X_ = [x for i, x in enumerate(X) if not L <= i <= R]
    X_.sort()
    X_used = [0]*len(X_)
    ans = 0
    for p in properties:
        for i in range(len(X_)):
            if X_used[i] == 0 and p[0] <= X_[i]:
                ans += p[1]
                X_used[i] = 1
                break
    print(ans)
