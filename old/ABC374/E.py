N, X = list(map(int, input().split()))
machines = [list(map(int, input().split())) for _ in range(N)]


# Wを達成するために必要な最低予算がX以下か
def condition(W):
    global machines, N, X

    budget = X
    for A, P, B, Q in machines:
        # Aの方が効率が良いこととしておく
        if A/P < B/Q:
            A, P, B, Q = B, Q, A, P
        
        # なるべく多くAを買う
        n = W//A+1
        
        # 最適とは限らないので１つずつ減らしながら探索を進める
        # 10個くらい調べたら打ち止め
        b = float('inf')
        for i in range(n, max(n-1000, -1), -1):
            tmp = W - A*i
            m = max(0, (tmp+B-1)//B)
            b = min(b, P*i+Q*m)
        
        budget -= b

        if budget < 0:
            return False
    
    return True


# 答えでにぶたん
ok = 0
ng = 10**12
while ng - ok > 1:
    test = (ng+ok)//2
    if condition(test):
        ok = test
    else:
        ng = test

print(ok)