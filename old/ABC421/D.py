# 線分同士の交点判定
def is_intersection(p1, p2, q1, q2):
    """
    線分P1P2と線分Q1Q2の交差判定
    端点を含めない場合はすべての<=を<で置換して使う
    """

    c1 = (p2[0] - p1[0]) * (q1[1] - p1[1]) - (p2[1] - p1[1]) * (q1[0] - p1[0])
    c2 = (p2[0] - p1[0]) * (q2[1] - p1[1]) - (p2[1] - p1[1]) * (q2[0] - p1[0])
    c3 = (q2[0] - q1[0]) * (p1[1] - q1[1]) - (q2[1] - q1[1]) * (p1[0] - q1[0])
    c4 = (q2[0] - q1[0]) * (p2[1] - q1[1]) - (q2[1] - q1[1]) * (p2[0] - q1[0])

    # 両方の線分が同一直線上にある場合
    if c1 == 0 and c2 == 0:
        # 1次元の射影が重なるかどうかを判定
        px = sorted([p1[0], p2[0]])
        qx = sorted([q1[0], q2[0]])
        py = sorted([p1[1], p2[1]])
        qy = sorted([q1[1], q2[1]])
        return (px[0] <= qx[1] and qx[0] <= px[1] and py[0] <= qy[1] and qy[0] <= py[1])

    # それ以外の場合はクロス積の符号で判定
    return c1 * c2 <= 0 and c3 * c4 <= 0

Rt, Ct, Ra, Ca = list(map(int, input().split()))
T = (Rt, Ct)
A = (Ra, Ca)
N, M, L = list(map(int, input().split()))

takahashi = [input().split() for _ in range(M)]
aoki = [input().split() for _ in range(L)]

if (Rt+Ct)%2 != (Ra+Ca)%2:
    print(0)
    exit()

takahashi = takahashi[::-1]
aoki = aoki[::-1]
tmp = takahashi.pop()
current_t = [tmp[0], int(tmp[1])]
tmp = aoki.pop()
current_a = [tmp[0], int(tmp[1])]

events = []
while takahashi or aoki:
    if current_t[1] == 0:
        tmp = takahashi.pop()
        current_t = [tmp[0], int(tmp[1])]
    
    if current_a[1] == 0:
        tmp = aoki.pop()
        current_a = [tmp[0], int(tmp[1])]
    

    n = min(current_t[1], current_a[1])
    events.append((current_t[0], current_a[0], n))
    current_t[1] -= n
    current_a[1] -= n

# U, D, R, Lを渡して移動後の座標を返す
def walk(now, direction, n):
    h, w = now
    walk_map = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    dh, dw = walk_map[direction]
    return (h+dh*n, w+dw*n)

ans = 0
for Dt, Da, n in events:
    T1 = walk(T, Dt, 1)
    A1 = walk(A, Da, 1)
    Tn = walk(T, Dt, n)
    An = walk(A, Da, n)

    if is_intersection(T1, Tn, A1, An):
        # 同じ方向
        if Dt == Da:
            # 同じスタート地点でなければならないが常に同じ場所
            if T == A:
                ans += n
        # 横に互い違い
        elif set([Dt, Da]) == set(['R', 'L']):
            ans += 1
        # 縦に互い違い
        elif set([Dt, Da]) == set(['U', 'D']):
            ans += 1
        # クロス
        else:
            # print('hoge')
            if Dt in ['U', 'D']:
                m = abs(A[0]-T[0])
            else:
                m = abs(A[1]-T[1])

            if walk(T, Dt, m) == walk(A, Da, m):
                ans += 1

    T = Tn
    A = An

print(ans)