N = int(input())

# 2点から直線を求める。1点目は(0, ans), 2点目は１つ目のビルの頂点で初期化
x1, y1 = 0, 0
x2, y2 = list(map(int, input().split()))

def get_line_param(x1, y1, x2, y2):
    a = (y2-y1)/(x2-x1)
    b = (x2*y1-x1*y2)/(x2-x1)
    return a, b

for _ in range(N-1):
    nx, H = list(map(int, input().split()))
    if y1*(x2-x1) + (y2-y1)*(nx-x1) < H*(x2-x1):
        _, y1 = get_line_param(x1, y1, x2, y2)
        x1 = 0
    else:
        x1, y1 = x2, y2

    x2, y2 = nx, H

if x1 == 0 and y1 == 0:
    print(-1)
else:
    _, ans = get_line_param(x1, y1, x2, y2)
    print(ans)