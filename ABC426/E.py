T = int(input())


def euclidian_d(u, v):
    return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5

def f1(TSx, TSy, dTx, dTy, ASx, ASy, dAx, dAy, t):
    return euclidian_d((TSx + dTx*t, TSy + dTy*t), (ASx + dAx*t, ASy + dAy*t))

def f2(TSx, TSy, dTx, dTy, AGx, AGy, t):
    return euclidian_d((TSx + dTx*t, TSy + dTy*t), (AGx, AGy))



for _ in range(T):
    TSx, TSy, TGx, TGy = list(map(int, input().split()))
    ASx, ASy, AGx, AGy = list(map(int, input().split()))
    TT = euclidian_d((TSx, TSy), (TGx, TGy))
    TA = euclidian_d((ASx, ASy), (AGx, AGy))
    # 必ず青木が先に着くように改ざん
    if TT < TA:
        TT, TA = TA, TT
        TSx, TSy, TGx, TGy, ASx, ASy, AGx, AGy = ASx, ASy, AGx, AGy, TSx, TSy, TGx, TGy

    # 青木がGに到達するまでの最小値を３分探索
    l,r=0, TA
    while l+0.00000001<r:
        c1=l+(r-l)/3
        c2=r-(r-l)/3
        if f1(TSx, TSy, (TGx-TSx)/TT, (TGy-TSy)/TT, ASx, ASy, (AGx-ASx)/TA, (AGy-ASy)/TA, c1) < f1(TSx, TSy, (TGx-TSx)/TT, (TGy-TSy)/TT, ASx, ASy, (AGx-ASx)/TA, (AGy-ASy)/TA, c2):
            r=c2
        else:
            l=c1
    res1 = f1(TSx, TSy, (TGx-TSx)/TT, (TGy-TSy)/TT, ASx, ASy, (AGx-ASx)/TA, (AGy-ASy)/TA, l)

    # 高橋がGに到達するまでの最小値を3分探索
    l,r=TA, TT
    while l+0.00000001<r:
        c1=l+(r-l)/3
        c2=r-(r-l)/3
        if f2(TSx, TSy, (TGx-TSx)/TT, (TGy-TSy)/TT, AGx, AGy, c1) < f2(TSx, TSy, (TGx-TSx)/TT, (TGy-TSy)/TT, AGx, AGy, c2):
            r=c2
        else:
            l=c1
    res2 = f2(TSx, TSy, (TGx-TSx)/TT, (TGy-TSy)/TT, AGx, AGy, l)
    print(min(res1, res2))