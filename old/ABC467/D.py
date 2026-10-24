T = int(input())
for _ in range(T):
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = list(map(int, input().split()))
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = 2*Px, 2*Py, 2*Qx, 2*Qy, 2*Rx, 2*Ry, 2*Sx, 2*Sy
    a = (Qx-Px, Qy-Py)
    b = (Sx-Rx, Sy-Ry)
    judge1 = a[0]*b[1] - a[1]*b[0] != 0
    
    ma = ((Qx+Px)//2, (Qy+Py)//2)
    mb = ((Sx+Rx)//2, (Sy+Ry)//2)
    m = (mb[0]-ma[0], mb[1]-ma[1])
    mi = (-m[1], m[0])
    judge2 = a[0]*mi[1] - a[1]*mi[0] == 0
    print('Yes' if judge1 or judge2  else 'No')
