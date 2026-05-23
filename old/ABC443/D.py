from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    R = list(map(tuple, enumerate(map(lambda x: int(x) - 1, input().split()))))
    dd = defaultdict(set)
    for i, v in R:
        dd[v].add(i)

    seen = [0]*N
    ans = 0
    # 上からi個目までに選ばれているものを確定させていく
    for h in range(N):
        target = h+1
        for c in dd[h]:
            seen[c] = 1
            # 両隣を前進させる
            for d_c in [-1, 1]:
                new_c = c + d_c
                if not 0 <= new_c < N:
                    continue
                if seen[new_c]:
                    continue

                i, v = R[new_c]
                if v <= target:
                    continue

                ans += v - target

                # 管理パラメータを更新
                dd[v].discard(new_c)
                dd[target].add(new_c)
                R[new_c] = (i, target)
                seen[new_c] = 1
        # print(ans, [v for i, v in R])
    print(ans)
                

