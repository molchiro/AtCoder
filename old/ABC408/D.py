T = int(input())

def solve(s):
    s = list(s)
    if '1' not in s:
        return 0
    
    # 両端の0を捨てる
    while s[-1] == '0':
        s.pop()
    s = s[::-1]
    while s[-1] == '0':
        s.pop()
    
    if '0' not in s:
        return 0

    # ランレングス圧縮
    rl = []
    prev = s[0]
    ct = 1
    for i in range(1, len(s)):
        c = s[i]
        if c == prev:
            ct += 1
        else:
            rl.append(ct)

            prev = c
            ct = 1
    rl.append(ct)

    if rl[0] > rl[-1]:
        rl = rl[::-1]

    

    # print(rl)

    # 今までまだ1の区間がない状態にするために必要なコストの最小値
    cost0 = 0
    # 1の区間繋がっている状態にするために必要なコストの最小値
    cost1 = 0
    # 0...1...0...の区間を作るために必要なコストの最小値
    cost010 = float('inf')
    # 1....0....の区間を作るために必要なコストの最小値
    cost10 = float('inf')
    for i in range(len(rl)//2):
        l1 = rl[2*i]
        l0 = rl[2*i+1]

        cost1 = min(cost1+l0, cost0+l0)

        cost010 = min(cost010+l1, cost0+0)

        cost10 = min(cost10+l1, cost1+0)

        cost0 += l1
    cost010 += rl[-1]
    cost10 += rl[-1]

    return min(cost0, cost1, cost010, cost10)


for _ in range(T):
    _ = int(input())
    S = input()
    print(solve(S))