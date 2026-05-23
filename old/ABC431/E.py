# (h, r, v(垂直or水平))の3次元頂点のグラフの問題としたとき、A ,B,C の種類次第で双方向に行き来できると考えられる
# とすると、どこの辺を切ったり張ったりするとSとGが連結になるかを考える問題になる
# 鏡を変えるとコスト１、そのままを０とすれば、0-1BFSで解ける!!

from collections import deque
wm = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

T = int(input())
for _ in range(T):
    H, W = list(map(int, input().split()))
    S = [input() for _ in range(H)]
    dq = deque()
    dq.append((0, 0, 'R', 0))
    seen = set()
    while dq:
        # print(dq)
        # input()
        h, w, d, cost = dq.popleft()
        if (h, w, d) in seen:
            continue
        seen.add((h, w, d))
        if (h, w, d) == (H-1, W, 'R'):
            print(cost)
            # print('next')
            break
        if (not 0 <= h < H) or (not 0 <= w < W):
            continue

        if d == 'R':
            for nd in ['R', 'L', 'U', 'D']:
                # 逆戻り不可
                if nd == 'L':
                    continue
                dh, dw = wm[nd]

                s = S[h][w]
                # cost
                if (nd, s) in [('R', 'A'), ('U', 'C'), ('D', 'B')]:
                    diff = 0
                else:
                    diff = 1
                
                if diff == 0:
                    dq.appendleft((h+dh, w+dw, nd, cost))
                else:
                    dq.append((h+dh, w+dw, nd, cost+1))
        elif d == 'L':
            for nd in ['R', 'L', 'U', 'D']:
                # 逆戻り不可
                if nd == 'R':
                    continue
                dh, dw = wm[nd]

                s = S[h][w]
                # cost
                if (nd, s) in [('R', 'A'), ('U', 'B'), ('D', 'C')]:
                    diff = 0
                else:
                    diff = 1
                
                if diff == 0:
                    dq.appendleft((h+dh, w+dw, nd, cost))
                else:
                    dq.append((h+dh, w+dw, nd, cost+1))
        elif d == 'U':
            for nd in ['R', 'L', 'U', 'D']:
                # 逆戻り不可
                if nd == 'D':
                    continue
                dh, dw = wm[nd]

                s = S[h][w]
                # cost
                if (nd, s) in [('U', 'A'), ('L', 'B'), ('R', 'C')]:
                    diff = 0
                else:
                    diff = 1
                
                if diff == 0:
                    dq.appendleft((h+dh, w+dw, nd, cost))
                else:
                    dq.append((h+dh, w+dw, nd, cost+1))
        else:
            for nd in ['R', 'L', 'U', 'D']:
                # 逆戻り不可
                if nd == 'U':
                    continue
                dh, dw = wm[nd]

                s = S[h][w]
                # cost
                if (nd, s) in [('D', 'A'), ('L', 'C'), ('R', 'B')]:
                    diff = 0
                else:
                    diff = 1
                
                if diff == 0:
                    dq.appendleft((h+dh, w+dw, nd, cost))
                else:
                    dq.append((h+dh, w+dw, nd, cost+1))

