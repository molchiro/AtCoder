def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b

def lcm(a, b):
    return int(a * b / gcd(a, b))

A, B, C, D = list(map(int, input().split()))
A_ = A - 1
lcm_CD = lcm(C, D)
B_res = B - (B//C + B//D - B//lcm_CD)
A_res = A_ - (A_//C + A_//D - A_//lcm_CD)
print(B_res - A_res)