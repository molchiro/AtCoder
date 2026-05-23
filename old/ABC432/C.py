N, X, Y = list(map(int, input().split()))
A = list(map(int, input().split()))
B = set(A)

def judge(test):
    global N, X, Y, B
    # アメの重さがtestグラムになるような組み合わせが全Bにわたって可能か判定
    for b in B:


ok = 0
ng = 10**18
while ng - ok > 1:
    test = (ng+ok)//2
    if condition:
        ok = test
    else:
        ng = test