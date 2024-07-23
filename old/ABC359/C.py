Sx, Sy = list(map(int, input().split()))
Tx, Ty = list(map(int, input().split()))
if (Sx+Sy)%2:
    Sx -= 1
if (Tx+Ty)%2:
    Tx -= 1
dx = abs(Sx-Tx)
dy = abs(Sy-Ty)

print(dy+max(dx-dy, 0)//2)
