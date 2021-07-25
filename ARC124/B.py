from collections import defaultdict
from copy import copy

# 左からi番目のビットでA, Bそれぞれをグループ分け
# 同じビット同士で組み合わせるか違うビット同士で組み合わせるかで分岐
# グループ同士の数が合わない時不成立
# 再帰で上位ビットから決定していく
# これで良い数になりうる数字が求まった
# 最後に条件成立するかチェック

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_bin = list(map(lambda x: ('0'*30 + bin(int(x))[2:])[-30:], A))
B_bin = list(map(lambda x: ('0'*30 + bin(int(x))[2:])[-30:], B))

can_good_n = []
def can_good(A, B, left):
    global can_good_n
    # left: 決定済みのビット列
    if A[0] == '':
        can_good_n.append(left)
        return
    
    A_0 = []
    A_1 = []
    B_0 = []
    B_1 = []
    for a, b in zip(A, B):
        if a[0] == '0':
            A_0.append(a[1:])
        else:
            A_1.append(a[1:])
        if b[0] == '0':
            B_0.append(b[1:])
        else:
            B_1.append(b[1:])
    
    if len(A_0) == len(B_0):
        if len(A_0) != 0:
            can_good(A_0, B_0, left+'0')
        else:
            can_good(A_1, B_1, left+'0')
    if len(A_0) == len(B_1):
        if len(A_0) != 0:
            can_good(A_0, B_1, left+'1')
        else:
            can_good(A_1, B_0, left+'1')

can_good(A_bin, B_bin, '')

B_kinds = defaultdict(int)
for b in B:
    B_kinds[b] += 1

good_n = []
for n in can_good_n:
    n = int(n, base=2)
    B_reminds = copy(B_kinds)
    for a in A:
        b = n ^ a
        B_reminds[b] -= 1
        if B_reminds[b] < 0:
            break
    else:
        good_n.append(n)
good_n.sort()
print(len(good_n))
if len(good_n) > 0:
    print(*good_n, sep='\n')
