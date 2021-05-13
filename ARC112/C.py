import sys
sys.setrecursionlimit(10**9)

N = int(input())
Children = [[] for i in range(N)]
Parent = [-1] + list(map(lambda x: int(x) - 1, input().split()))
for i in range(1, N):
    Children[Parent[i]].append(i)

def solve(v):
    # vを根とする部分木において、(手番が入れ替わるかどうか, 先手-後手の得点) を返す
    # まず先手が１取った後、後手の最適な指し方をシミュレートする
    res = 1
    # pos: 得点差が正で手番が入れ替わらない
    # neg: 得点差が負で手番が入れ替わらない
    # sw: 手番が入れ替わる
    pos = []
    neg = []
    sw = []
    for c in Children[v]:
        f, score = solve(c)
        if f:
            sw.append(score)
        elif score < 0:
            neg.append(score)
        else:
            pos.append(score)
    # まず後手はnegを総取り
    res += sum(neg)
    # sw を交互に取り合う
    # f = 0:先手 1:後手
    sw.sort()
    f = 1
    for score in sw:
        if f:
            res += score
        else:
            res -= score
        f = 1-f
    # 最後にposを総取り
    if f:
        res += sum(pos)
    else:
        res -= sum(pos)
    
    return f, res

# T = 先手-後手, N = 先手+後手より、N+T = 2*先手
_, T = solve(0)
print((N+T)//2)