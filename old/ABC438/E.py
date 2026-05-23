N, Q = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))
doubling_v = [[i+1 for i in range(N)]]
doubling_p = [[A[i] for i in range(N)]]

for i in range(32):
    doubling_v_next = [doubling_v[-1][i] + doubling_v[-1][doubling_p[-1][i]] for i in range(N)]
    doubling_v.append(doubling_v_next)
    doubling_p_next = [doubling_p[-1][doubling_p[-1][i]] for i in range(N)]
    doubling_p.append(doubling_p_next)

for _ in range(Q):
    T, B = list(map(int, input().split()))
    now = B-1
    ans = 0
    for i in range(32):
        if T%2:
            ans += doubling_v[i][now]
            now = doubling_p[i][now]
        T //= 2
    print(ans)