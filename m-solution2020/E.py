from itertools import product

INF_D = 100000
N = int(input())
villages = [list(map(int, input().split())) for _ in range(N)]

# 方針 集落と集落の間を通るよりも集落を通り抜ける方が良いのは確実
# 集落を通る鉄道の候補を列挙し、bit全探索する
all_rails = []
for x in set(map(lambda village: village[0], villages)):
    all_rails.append([x, INF_D])
for y in set(map(lambda village: village[1], villages)):
    all_rails.append([INF_D, y])
all_rails_N = len(all_rails)
# print(all_rails)

def S(villages, rails):
    ans = 0
    # print(villages)
    # print(rails)
    for village in villages:
        min_D = INF_D
        X, Y, P = village
        for rail in rails:
            min_D = min(min_D, abs(rail[0]-X), abs(rail[1]-Y))
            if min_D == 0:
                break
        # print(min_D)
        ans += P*min_D
    return ans

K_rails = [[] for _ in range(N+1)]
for rails_bit in product([0, 1], repeat=all_rails_N):
    rails = [all_rails[i] for i in range(all_rails_N) if rails_bit[i]]
    rails_N = len(rails)
    if rails_N <= N:
        K_rails[sum(rails_bit)].append([[0, INF_D], [INF_D, 0]] + rails)
# print(*K_rails, sep='\n')
for i in range(N+1):
    ans = 10**11
    for rails in K_rails[i]:
        ans = min(ans, S(villages, rails))
    print(ans)
