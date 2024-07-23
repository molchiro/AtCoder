H, W, N = list(map(int, input().split()))
T = input()

field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            field[h+1][w+1] = -1

ans = 0
for h in range(H):
    for w in range(W):
        now = [h+1, w+1]
        for t in T:
            if field[now[0]][now[1]] == -1:
                break
            if t == 'U':
                now[0] -= 1
            elif t == 'D':
                now[0] += 1
            elif t == 'R':
                now[1] += 1
            else:
                now[1] -= 1
            
            if field[now[0]][now[1]] == -1:
                break
        else:
            ans += 1
            # print(h+1, w+1)

print(ans)