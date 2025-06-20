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

    # (gp, gc)で辺を並び替え
    sorted_edges = []
    for p, c in edges:
        grade_p = grade(A[p], limits)
        grade_c = grade(A[c], limits)

        # cの方が美しくなるようにswap
        if grade_p > grade_c:
            p, c = c, p
            grade_p, grade_c = grade_c, grade_p

        sorted_edges.append(((grade_p, grade_c), (p, c)))
        sorted_edges.append(((grade_c, grade_p), (c, p)))
    sorted_edges.sort()

    p_list = [-1]*N
    h_list = [-1]*N

    # なるべく階段上になるように辺を結ぶ試行を繰り返す
    for i in range(20):
        unused_edges = []
        for (grade_p, grade_c), (p, c) in sorted_edges:
            # 子の高さが決まっているならスキップ
            if h_list[c] >= 0:
                continue
            # 親の高さが10以上ならスキップ
            if h_list[p] >= 10:
                continue

            # 親のグレードがゼロなら高さ0を確定させる
            if grade_p == 0:
                h_list[p] = 0

            # 親の高さが決まっていて、その高さが子のグレードの１つ下であるか確認
            if h_list[p] >= 0 and grade_c - h_list[p] ==  1:                
                h_list[c] = h_list[p] + 1
                p_list[c] = p
            else:
                # 使わなかった辺は取っておく
                unused_edges.append(((grade_p, grade_c), (p, c)))
                    
        next_edges = []

        # 続いて同じ階層以下の辺を使って高さを稼ぐ
        for (grade_p, grade_c), (p, c) in unused_edges:
            if h_list[p] >= 0 and grade_c - h_list[p] <= 0 :
                # cの高さが決まっているなら何もしない
                if h_list[c] >= 0:
                    continue

                # pがすでに高さ10ならなにもしない
                if h_list[p] >= 10:
                    continue

                p_list[c] = p
                h_list[c] = h_list[p] + 1

            else:
                next_edges.append(((grade_p, grade_c), (p, c)))

        # print(*p_list)

        # 次のループの準備
        sorted_edges = next_edges

    # 20周しても連結できなかった頂点は適当に繋ぐ
    G = [[] for _ in range(N)]
    for u, v in edges:
        G[u].append(v)
    
    for i in range(N):
        if h_list[i] == -1:
            h_max = -1
            p = -1
            # 連結な頂点の中で一番高い頂点と接続する
            for to in G[i]:
                h_to = h_list[to]
                if h_to >= 10:
                    continue
                if h_to > h_max:
                    h_max = h_to
                    p = to
            # どことも連結できなかった場合は自分が根になる
            if h_max == -1:
                h_list[i] = 0
                p_list[i] = -1
            else:
                h_list[i] = h_max + 1
                p_list[i] = p

    score = 1
    for i in range(N):
        if h_list[i] == -1:
            h_list[i] = 0
        score += A[i]*(h_list[i]+1)

    return score, p_list

# 初期解を均等分の区間で出す
max_score, ans = solve([9, 18, 27, 36, 45, 54, 63, 72, 81, 90])
# 区間を自動生成して時間の許す限り試す
while time.time() - start_time < 1.8:
    limits = generate_limits()
    limits.sort()
    # print(limits)
    s, p = solve(limits)
    if s > max_score:
        # print('better!!')
        ans = p

# print(max_score)
print(*ans)