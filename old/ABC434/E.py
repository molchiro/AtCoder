# ユニーク位置をもつうさぎの行先を先に決める
# そのうさぎがいないとして、もう一度ユニーク位置を探す

N = int(input())
rabbits = [list(map(int, input().split())) for _ in range(N)]

from collections import defaultdict

dd = defaultdict(set)

for i, (x, r) in enumerate(rabbits):
    dd[x+r].add(i)
    dd[x-r].add(i)

ans = 0
seen = [0]*N

f = 1
while f:
    f = 0
    stack = []
    for k, v in dd.items():
        if len(v) == 1:
            stack.append(list(v)[0])
            f = 1
    

    while stack:
        # print(stack)
        v = stack.pop()
        id = v
        if seen[id]:
            continue
        seen[id] = 1

        x, r = rabbits[id]
        dd[x+r].remove(id)
        dd[x-r].remove(id)
        ans += 1
        if len(dd[x+r]) == 0:
            del dd[x+r]
        elif len(dd[x+r]) == 1:
            stack.append(list(dd[x+r])[0])
        if len(dd[x-r]) == 0:
            del dd[x-r]
        elif len(dd[x-r]) == 1:
            stack.append(list(dd[x-r])[0])

ans += len(dd.items())
        
print(ans)

