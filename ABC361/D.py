# 考えうる文字をノードとする
# 初期値をスタートのノードとする
# 連続する場所と..を入れ替えるてできた文字のノードと連結する
# 初めて辿り着いたノードならqueueに追加する
# FIFOキューを全て処理する

from collections import deque

N = int(input())
S = input() + '..'
T = input() + '..'

def swap(text):
    text = 'X..' + text +'..X'
    _, l, r, _ = text.split('..')
    # print(l, r, len(l), len(r)) 
    res = []
    if len(l) >= 2:
        for i in range(len(l)-1):
            res.append(l[:i] + '..' + l[i+2:] + l[i:i+2] + r)
    if len(r) >= 2:
        for i in range(len(r)-1):
            res.append(l + r[i:i+2] + r[:i] + '..' + r[i+2:])
    
    return res

# print(swap(S))
# print(swap('BB..WW'))

dq = deque([S])
d = dict()
d[S] = 0
while(dq):
    # print(dq)
    u = dq.popleft()
    k = d[u]

    for v in swap(u):

        if v in d.keys():
            continue

        d[v] = k+1
        dq.append(v)

if T in d.keys():
    print(d[T])
else:
    print(-1)

