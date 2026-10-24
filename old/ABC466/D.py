N, M = list(map(int, input().split()))

actions = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

# 取り除く操作のカウント
# ans = N*N
# tate = [1]*N
# tate_accum = N
# yoko = [1]*N
# yoko_accum = N
# for R, C in actions:
#     if tate[C]:
#         ans -= yoko_accum
#         tate[C] = 0
#         tate_accum -= 1
#         # print('tate', ans)
#     if yoko[R]:
#         ans -= tate_accum
#         yoko[R] = 0
#         yoko_accum -= 1
        # print('yoko', ans)
        
#     print(tate, tate_accum)
#     print(*yoko, sep='\n')
#     print(yoko_accum)
# print(ans)

ans = 0

# 置く操作は逆順に再現
tate = [1]*N
yoko = [1]*N
while actions:
    R, C = actions.pop()
    if tate[C] and yoko[R]:
        ans += 1
    tate[C] = 0
    yoko[R] = 0
    # print(tate)
    # print(*yoko, sep='\n')
    # print(ans)

print(ans)
