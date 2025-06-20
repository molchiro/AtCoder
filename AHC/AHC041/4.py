from collections import deque
import random
import time
start_time = time.time()
rng = random.Random(1234)

N, M, H = list(map(int, input().split()))
A = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]
points = [list(map(int, input().split())) for _ in range(N)]

def generate_limits():
    global rng
    return rng.sample(range(1, 101), 10)

def grade(x, limits):

    for i, limit in enumerate(limits):
        if x <= limit:
            return i
    return 10


# 11段階を分ける閾値のリスト（長さ10)
def solve(limits):
    global N, M, H
    global A
    global edges

    graded_edges = [[] for _ in range(11)]
    grades = [grade(a, limits) for a in A]

    for i, (u, v) in enumerate(edges):
        graded_edges[grades[u]].append((i, u, v))
        graded_edges[grades[v]].append((i, v, u))

    # print(graded_edges)

    p_list = [-1]*N
    h_list = [-1]*N

    # グレード0を根とする
    for i in range(N):
        if grades[i] == 0:
            h_list[i] = 0

    # グレードの低い辺を優先的に使って高さを稼ぐ
    dq = deque()
    for i in range(11):
        dq.extend(graded_edges[i][:])
        # グレードが高いものを先に使ってしまわないよう、グレードの差がないものを優先的に使う
        for d in range(i+1):

            prev = dq[-1][0]
            # 変化がなくなるまで全ての辺を探索
            while dq and prev != dq[0][0]:                
                edge_id, u, v = dq.popleft()

                # # 行き先のグレードがiで高さ未定なら根とする
                # if grades[v] == i and h_list[v] == -1:
                #     h_list[v] = 0

                # 行き先の高さが決まっていないなら後回し
                if h_list[v] == -1:
                    dq.append((edge_id, u, v))
                    continue

                # 自分の高さが決まっているなら辺を捨てる
                if h_list[u] >= 0:
                    continue

                # 行き先の高さが10以上なら辺を捨てる
                if h_list[v] >= 10:
                    continue
            
                # 行き先と自分のグレードの差がd以下なら消費
                if grades[u] - h_list[v] <=  d:
                    prev = edge_id              
                    h_list[u] = h_list[v] + 1
                    p_list[u] = v

        print(p_list)
                        
    # print(h_list)

    score = 1
    for i in range(N):
        if h_list[i] == -1:
            h_list[i] = 0
        score += A[i]*(h_list[i]+1)

    return score, p_list

# 初期解を均等分の区間で出す
max_score, ans = solve([9, 18, 27, 36, 45, 54, 63, 72, 81, 90])
# 区間を自動生成して時間の許す限り試す
# while time.time() - start_time < 1.8:
#     limits = generate_limits()
#     limits.sort()
#     # print(limits)
#     s, p = solve(limits)
#     if s > max_score:
#         # print('better!!')
#         ans = p

# print(max_score)
print(*ans)