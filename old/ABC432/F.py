import sys
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))
B = sum(A)//N
if B*N != sum(A):
    print(-1)
    exit()
res = []
m = 10**18
# seen = set()
# ちょうどBの子は終了、Bより多く持っている子から少ない子に余剰を全部渡すパターンを総当たりして、操作回数が少ないものが答え
def solve(jotai, sousa=[]):
    # print(jotai)
    global N, A, B, res, m
    # if tuple(jotai) in seen:
    #     return
    # seen.add(tuple(jotai))

    if len(sousa) >= m:
        return

    yojo = [i for i in range(N) if jotai[i] > B]
    kasho = [i for i in range(N) if jotai[i] < B]

    if len(sousa) + max(len(yojo), len(kasho)) >= m:
        return

    if yojo == [] and kasho == []:
        res.append(sousa[:])
        m = min(m, len(sousa))
        return
    
    for x in sorted(yojo, key=lambda x: -jotai[x]):
        z = jotai[x] - B

        for y in kasho:
            if jotai[y] + z == B:
                new_jotai = jotai[:]
                new_jotai[x] -= z
                new_jotai[y] += z
                solve(new_jotai, sousa[:]+[(x+1, y+1, z)])
                break
        else:
            for y in sorted(kasho, key=lambda x: jotai[x]):
                new_jotai = jotai[:]
                new_jotai[x] -= z
                new_jotai[y] += z
                solve(new_jotai, sousa[:]+[(x+1, y+1, z)])
            

solve(A)
res.sort(key=lambda x: len(x))
ans = res[0]
# print(ans)
print(len(ans))
for sousa in ans:
    print(*sousa)