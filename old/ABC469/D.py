N, M = list(map(int, input().split()))
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

ans = 0
# 1個目の左を選んだ時
selected_1 = AB[0][0]
CD = [(a, b) for a, b in AB[1:] if a != selected_1 and b != selected_1]
if CD:
    # 2個目の左を選んでEFが空ならOK
    selected_2 = CD[0][0]
    EF = [(a, b) for a, b in CD[1:] if a != selected_2 and b != selected_2]
    if not EF:
        ans += 1
    # 右も同じ
    selected_2 = CD[0][1]
    EF = [(a, b) for a, b in CD[1:] if a != selected_2 and b != selected_2]
    if not EF:
        ans += 1
else:
    # CDが空なら残り全部使える
    ans += N-1

# print(ans)

# 1個目の右を選んだ時
selected_1 = AB[0][1]
CD = [(a, b) for a, b in AB[1:] if a != selected_1 and b != selected_1]
# print(CD)
if CD:
    # 2個目の左を選んでEFが空ならOK
    selected_2 = CD[0][0]
    EF = [(a, b) for a, b in CD[1:] if a != selected_2 and b != selected_2]
    if not EF:
        ans += 1
    # 右も同じ
    selected_2 = CD[0][1]
    EF = [(a, b) for a, b in CD[1:] if a != selected_2 and b != selected_2]
    if not EF:
        ans += 1
else:
    # CDが空なら残り全部使える
    ans += N-1

# print(ans)

# 1個目の2つを選んでも良いなら上記の選択に重複がある
CD = [(a, b) for a, b in AB[1:] if a not in AB[0] and b  not in  AB[0]]
if not CD:
    ans -= 1

print(ans)