def manhattan_d(u, v):
    return abs(v[0]-u[0])+abs(v[1]-u[1])

Xa, Ya, Xb, Yb, Xc, Yc = list(map(int, input().split()))

# Cが原点に重なるよう並行移動
Xa -= Xc
Ya -= Yc
Xb -= Xc
Yb -= Yc
# Bが第一象限に来るまで回転
while Xb < 0 or Yb < 0:
    Xb, Yb = -Yb, Xb
    Xa, Ya = -Ya, Xa

# print(Xa, Ya, Xb, Yb)

# Bを押す位置に移動するまでの移動距離とBを押す距離を分けて考える
# まずBを押す距離
ans = Xb+Yb
# 次にBを押す位置に移動するまでの移動距離
# y軸上
if Xb == 0:
    # Aが半直線BC上にある時は迂回が必要
    if Xa == 0 and Ya < Yb:
           ans += 2
    ans += manhattan_d((Xa, Ya), (0, Yb+1)) 
# x軸上
elif Yb == 0:
    # Aが半直線BC上にある時は迂回が必要
    if Ya == 0 and Xa < Xb:
           ans += 2
    ans += manhattan_d((Xa, Ya), (Xb+1, 0))
else:
    ans += min(manhattan_d((Xa, Ya), (Xb+1, Yb)), manhattan_d((Xa, Ya), (Xb, Yb+1)))
    # 押す方向を変える距離
    ans += 2

print(ans)