H, W = list(map(int, input().split()))

# -1: #
# 0: .
# 1: o
# 2: x
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]

for h in range(H):
    row = input()

    for w in range(W):
        if row[w] == '#':
            field[h+1][w+1] = -1
        elif row[w] == 'o':
            field[h+1][w+1] = 1
        elif row[w] == 'x':
            field[h+1][w+1] = 2
        elif row[w] == 'S':
            S = (h+1, w+1)
        elif row[w] == 'G':
            G = (h+1, w+1)

mp = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
mp_index = {'U': 0, 'D': 1, 'R': 2, 'L': 3}

history = [[[None]*4 for _ in range(W+2)] for _ in range(H+2)]
seen = [[[0]*4 for _ in range(W+2)] for _ in range(H+2)]

from collections import deque

dq = deque()
dq.append((S, 'U'))


def can_go(v, d):
    global field, history

    h, w = v

    if field[h][w] == -1 or seen[h][w][mp_index[d]]:
        return 0
    else:
        return 1
    
def priority(u):
    global G

    if u[0] < G[0]:
        return ['R', 'U', 'D', 'L']
    elif u[0] > G[0]:
        return ['L', 'U', 'D', 'R']
    elif u[0] > G[0]:
        return ['U', 'R', 'L' 'D']
    else:
        return ['D', 'R', 'L', 'U']


while dq:
    u, d = dq.popleft()
    if u == G:
        break

    h, w = u
    if field[h][w] == 0:
        for i in range(4):
            seen[h][w][i] = 1

    else:
        seen[h][w][mp_index[d]] = 1

    # oマス
    if field[h][w] == 1:
        nxt_d = d
        dh, dw = mp[nxt_d]
        v = (h+dh, w+dw)
        if not can_go(v, nxt_d):
            continue

        history[v[0]][v[1]][mp_index[nxt_d]] = (u, d, nxt_d)
        dq.append((v, nxt_d))
    
    elif field[h][w] == 2:
        # xマス
        for nxt_d in priority(u):
            if nxt_d == d:
                continue

            dh, dw = mp[nxt_d]
            v = (h+dh, w+dw)
            if not can_go(v, nxt_d):
                continue

            history[v[0]][v[1]][mp_index[nxt_d]] = (u, d, nxt_d)
            dq.append((v, nxt_d))
            
    else:
        for nxt_d in priority(u):

            dh, dw = mp[nxt_d]
            v = (h+dh, w+dw)
            if not can_go(v, nxt_d):
                continue

            history[v[0]][v[1]][mp_index[nxt_d]] = (u, d, nxt_d)
            dq.append((v, nxt_d))

# print(history)

gh, gw = G
for i in range(4):
    if history[gh][gw][i] == None:
        continue


    ans = []
    u, d, nxt_d = history[gh][gw][i]
    ans.append(nxt_d)
    while u != S:
        v, d, nxt_d = history[u[0]][u[1]][mp_index[d]]
        ans.append(nxt_d)
        u = v
        # print(ans)
    
    print('Yes')
    print(''.join(ans[::-1]))
    exit()


else:
    print('No')
