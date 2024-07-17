A, B, C, D = list(map(int, input().split()))
A_offset = A - A%4
C -= A_offset
A -= A_offset
B_offset = B - B%2
D -= B_offset
B -= B_offset

ans = 0

def culc_sub(x, y):
    rect = [[2, 1, 0, 1], [1, 2, 1, 0]]
    res = 0
    for i in range(x):
        for j in range(y):
            res += rect[j][i]
    return res

def culc(x, y):
    res = 0
    # 完全な長方形部分
    res += culc_sub(4, 2)*(x//4)*(y//2)
    # 上の中途半端な部分
    res += culc_sub(4, y%2)*(x//4)
    # 右の中途半端な部分
    res += culc_sub(x%4, 2)*(y//2)
    # 右上の中途半端な部分
    res += culc_sub(x%4, y%2)
    return res

ans = 0
# 包除原理
ans += culc(C, D)
ans -= culc(A, D)
ans -= culc(C, B)
ans += culc(A, B)
print(ans)


