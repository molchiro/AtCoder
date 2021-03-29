import numpy as np

def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])

    return  np.dot(R, u)

N = int(input())
x0, y0 = list(map(int, input().split()))
xm, ym = list(map(int, input().split()))
O = ((x0+xm)/2, (y0+ym)/2)
ans = (x0-O[0], y0-O[1])
ans = rotation_o(ans, 360/N, deg=True)
ans = (ans[0]+O[0], ans[1]+O[1])
print(*ans)