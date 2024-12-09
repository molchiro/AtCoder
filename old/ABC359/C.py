Sx, Sy = list(map(int, input().split()))
Tx, Ty = list(map(int, input().split()))

# x座標を左側にシフトしておく
if (Sx+Sy)%2:
    Sx -= 1
if (Tx+Ty)%2:
    Tx -= 1

dx = abs(Sx-Tx)
dy = abs(Sy-Ty)

if dx < dy:
    print(dy)
else:
    print(dy+(dx-dy)//2)
