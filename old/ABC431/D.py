from collections import defaultdict

N = int(input())
parts = [list(map(int, input().split())) for _ in range(N)]

# 全てボディにつけた状態を初期状態とし、頭に付け替えた場合でdp
# dp[i][dw]: i番目までみたとき、ボディの方がdwだけ大きい時の嬉しさの最大

dp = defaultdict(int)
dp[sum([w for w, _, _ in parts])] = sum([b for _, _, b in parts])

for w, h, b in parts:
    ndp = dp.copy()

    for dw, v in dp.items():
        if dw - 2*w < 0:
            continue

        ndp[dw-2*w] = max(ndp[dw-2*w], v + h-b)

    dp = ndp

print(max(dp.values()))