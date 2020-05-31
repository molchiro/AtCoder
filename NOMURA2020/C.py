N = int(input())
A = list(map(int, input().split()))
if N == 0 and A[0] == 1:
    print(1)
else:
    nodes = [0]*(N+1)
    s_d = 0 # 飽和してないノードが残ってる深さ
    cap_d = 1 - A[0]
    failed = False
    for i, a in enumerate(A):
        # a個の葉をなるべく浅いノードから取る
        while a > 0:
            # これ以上分岐することろがなければ失敗
            if i < s_d or cap_d <= 0:
                failed = True
                break
            # s_dから枝を取れるだけ取る
            x = min(cap_d - nodes[s_d], a)
            a -= x
            nodes[s_d:i+1] = [node + x for node in nodes[s_d:i+1]]
            # s_dがいっぱいになったら深さを一つ進める
            if nodes[s_d] >= cap_d:
                cap_d -= A[s_d]
                cap_d *= 2
                s_d += 1
        if failed:
            break
    print(-1 if failed else sum(nodes))