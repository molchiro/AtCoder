from collections import defaultdict
N, M = list(map(int, input().split()))
blacks = defaultdict(list)
for _ in range(M):
    x, y = list(map(int, input().split()))
    blacks[x].append(y)


# sectionss: 白ポーンが存在しうる区間[[始点1, 終点1],,, ]
sections = [[N, N]]
prev_row = 0
x_has_blacks = list(blacks.keys())
x_has_blacks.sort()
for x in x_has_blacks:
    # 直進できる区間をとる
    tmp = []
    blacks_in_this_row = blacks[x]
    for l, r in sections:
        for y in [y for y in blacks_in_this_row if l <= y <= r]:
            # print(l, r, y)
            if l <= y-1:
                tmp.append([l, y-1])
            l = y+1
        if l <= r:
            tmp.append([l, r])
    straight = tmp[:]
    # print(straight)
    
    # 斜め移動できる箇所をとる
    y_set = set(blacks_in_this_row)
    naname = []
    for l, r in sections:
        if l == r:
            naname += [[y, y] for y in y_set if y in [l-1, l+1]]
        else:
            naname += [[y, y] for y in y_set if y in range(l-1, r+2)]
    # print(naname)
    # 区間をマージ
    st_nana = []
    if straight != []:
        st_nana += straight
    if naname != []:
        st_nana += naname
    # print(st_nana)
    if st_nana == []:
        print(0)
        exit()
    st_nana.sort()
    tmp = [[-float('inf'), -float('inf')]]
    for l, r in st_nana:
        if l-1 > tmp[-1][1]:
            tmp.append([l, r])
        else:
            tmp[-1][1] = max(r, tmp[-1][1])
    # print(tmp)
    sections = tmp[1:]
    # print(sections)

# print(sections)
ans = 0
for l, r in sections:
    ans += r-l+1
print(ans)