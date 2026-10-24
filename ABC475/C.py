N, S, L = list(map(int, input().split()))
A = list(map(int, input().split()))

def solve(array, n, s, l):
    cumsum = [0]
    for x in array:
        cumsum.append(cumsum[-1] + x)

    res = 0

    cumsum.append(10**20)
    # print(array, s, cumsum)

    # 指定しただけ左に行く
    for i in range(s+1):
        cost = cumsum[s] - cumsum[i]
        if cost > l:
            continue

        # 行けるだけ右に行く
        ok = 0
        ng = n+1
        while ng - ok > 1:
            test = (ng+ok)//2
            if cost + cumsum[test] - cumsum[i] <= l:
                ok = test
            else:
                ng = test

        # print(s, i, ok, cost, max(ok, s)-i+1)
        res = max(res, max(ok, s)-i+1)

    return res


res1 = solve(A, N, S-1, L)
A = A[::-1]
res2 = solve(A, N, N-S, L)
# print(res1, res2)
print(max(res1, res2))