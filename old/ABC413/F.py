from collections import deque

def move(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]


H, W, K = list(map(int, input().split()))

# 場外または千日手確定が-1, 未定はinf
field = [[-1]*(W+2)] + [[-1]+ [float('inf')]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
ct = [[-5]*(W+2)] + [[-5]+ [0]*W + [-5] for _ in range(H)] + [[-5]*(W+2)]

dq = deque()

for _ in range(K):
    h, w = list(map(int, input().split()))
    field[h][w] = 0
    ct[h][w] = 4
    dq.append((h, w))
    
ans = 0
while dq:
    h, w = dq.popleft()

    # 周囲を探索
    for nh, nw in move(h, w):
        ct[nh][nw] += 1
        # 二個目に確定したところに到達可能
        if ct[nh][nw] == 2 and field[nh][nw] == float('inf'):
            dq.append((nh, nw))
            field[nh][nw] = field[h][w] + 1
            ans += field[nh][nw]

print(ans)


