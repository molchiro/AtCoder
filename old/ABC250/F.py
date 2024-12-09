N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
# x軸より上に来るように平行移動
y_min = min([p[1] for p in points])
if y_min < 0:
    for i in range(N):
        points[i][1] -= y_min 

# 扱いやすいように左端の点が0番目になるように調整
x_min = min([p[0] for p in points])
x_min_index = 0
while points[x_min_index][0] != x_min:
    x_min_index += 1
points = points[x_min_index:]+points[:x_min_index]
points.append(points[0])

# 右端の点のindexを出しておく
x_max = max([p[0] for p in points])
x_max_index = 0
while points[x_max_index][0] != x_max:
    x_max_index += 1

# N角形の面積を求める（２倍でOK
S = 0
for i in range(x_max_index, N):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    S += (y1+y2)*abs(x1-x2)
for i in range(x_max_index):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    S -= (y1+y2)*abs(x1-x2)

# 2点を選んで切ったうち小さい方の面積を求める関数を作る（２倍でOK

def culc(a, b):
    global points, S
    if a > b:
        a, b = b, a
    
    if

# 1点を固定して全探索
    # まずは半分に近い点を求める
    # その左側の中から一番1/4に近い点を探す
    # 右側も同様
