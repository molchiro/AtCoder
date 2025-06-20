N = int(input())
A = list(map(int, input().split()))

ans = 0

def solve(l):
    if len(l) == 0:
        return
    global N, A
    global ans

    odds = []
    total_o = 0
    evens = []
    total_e = 0
    for x in l:
        if x%2:
            odds.append(x)
            total_o += x
        else:
            evens.append(x)
            total_e += x
    ans += total_e*len(odds) + total_o
    print(ans, odds, evens)
    # 偶数の部分列は２で割ってもう一度
    solve([x for x in [x//2 for x in evens] if x > 0])

    # 奇数の部分列は割った次のビットが立っているかで分類
    next_odds = []
    next_evens = []
    total_n_o = 0
    total_n_e = 0
    for x in odds:
        if x%2:
            next_odds.append(x)
            total_n_o += x
        else:
            next_evens.append(x)
            total_n_e += x

    # 次のビットが立っているもの同士はどう組み合わせても次で終わるのが確定する
    tmp = total_n_o
    for x in next_odds:
        ans += x//2
        ans += tmp//2
        tmp -= x
    # 次のビットが立っていないもの同士も同様
    tmp = total_n_e
    for x in next_evens:
        ans += x//2
        ans += tmp//2
        tmp -= x
    
    solve([x for x in [x//2 + 1 for x in next_evens] + [x//2 for x in next_odds] if x > 0])

solve(A)
print(ans)
