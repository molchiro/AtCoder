from math import gcd

def lcm(a, b):
    return int(a * b / gcd(a, b))

N = int(input())
card_packs = [tuple(map(int, input().split())) for _ in range(N)]

# i-1番目まででありえるgcdの組み合わせとi番目の袋からの取り出し方の組み合わせを全て試す
dp = [set() for _ in range(N)]
dp[0].add(card_packs[0])

def f(prev_gcds, pack):
    ret = []
    for X, Y in prev_gcds:
        ret.append((gcd(X, pack[0]), gcd(Y, pack[1])))
        ret.append((gcd(X, pack[1]), gcd(Y, pack[0])))
    ret= set([tuple(sorted(x)) for x in ret])
    return ret

for i in range(1, N):
    pack = card_packs[i]
    dp[i] = f(dp[i-1], pack)

ans = 0
for X, Y in dp[-1]:
    ans = max(ans, lcm(X, Y))
print(ans)