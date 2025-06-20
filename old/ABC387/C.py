def culc(x):
    # x以下のへび数の数を求める
    if x < 10:
        return 0
    
    res = 0

    d = len(str(x))

    # d-1桁までは何も考えずに足し合わせる
    for i in range(1, d-1):
        for head in range(1, 10):
           res += head**i

    # ちょうどd桁の数については上の桁から考える
    # 最上位の数字がxの最上位よりも小さければ何も考えずに足せる
    for head in range(1, int(str(x)[0])):
        res += head**(d-1)

    tmp1 = 1
    tmp2 = 0
    head = int(str(x)[0])
    for i in range(1, d):
        y = int(str(x)[i])
        tmp2 *= head
        if tmp1:
            if y >= head:
                tmp1 = 0
                tmp2 += head
            else:
                tmp2 += y

    res += tmp1+tmp2

    return res

assert culc(100) == 46, culc(100)
assert culc(99) == 45, culc(99)
assert culc(98) == 45, culc(98)
assert culc(200) == 47, culc(200)
assert culc(201) == 48, culc(201)
assert culc(202) == 48, culc(202)
assert culc(210) == 49, culc(210)
assert culc(211) == 50, culc(211)
assert culc(212) == 50, culc(212)
assert culc(220) == 50, culc(220)
assert culc(300) == 51, culc(300)
assert culc(303) == 53, culc(303)
assert culc(310) == 54, culc(310)
assert culc(311) == 55, culc(311)
assert culc(320) == 57, culc(320)
assert culc(321) == 58, culc(321)
assert culc(322) == 59, culc(322)
assert culc(323) == 59, culc(323)
assert culc(329) == 59, culc(329)
assert culc(330) == 59, culc(330)
assert culc(331) == 59, culc(331)
assert culc(333) == 59, culc(333)
assert culc(399) == 59, culc(399)
assert culc(499) == 75, culc(499)
assert culc(599) == 100, culc(599)
assert culc(699) == 136, culc(699)
assert culc(799) == 185, culc(799)
assert culc(899) == 249, culc(899)
assert culc(999) == 330, culc(999)
assert culc(1000) == 331, culc(1000)
assert culc(9999) == 2355, culc(9999)

L, R = list(map(int, input().split()))
print(culc(R)-culc(L-1))