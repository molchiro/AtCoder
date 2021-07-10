from collections import deque

N = int(input())
S = [input() for _ in range(N)]
head_dict = {}
head_keys = set()
tail_dict = {}
tail_keys = set()
for i, s in enumerate(S):
    head = s[:3]
    tail = s[-3:]
    # print(head, tail)
    if head in head_keys:
        head_dict[head].append(i)
    else:
        head_keys.add(head)
        head_dict[head] = [i]
    if tail in tail_keys:
        tail_dict[tail].append(i)
    else:
        tail_keys.add(tail)
        tail_dict[tail] = [i]
    
result = [None]*N
lose_dd = deque()
# まず絶対勝つやつを決める
for i, s in enumerate(S):
    head = s[:3]
    tail = s[-3:]
    if tail not in head_keys:
        result[i] = 1
        # tailがこの単語のheadになっているやつは負け確定
        if head in tail_keys:
            lose_dd.append(head)
            # 確定済みのものは削除して枝切り
            tail_keys.remove(head)
        # 確定済みのものは削除して枝切り
        if tail in tail_keys:
            tail_keys.remove(tail)


        
# print(result)

# 以降、負けが確定したやつを決める=>その単語にしかいけないやつは勝ち=>その単語にしかいけないやつは負けを繰り返す
while lose_dd:
    # print(lose_dd)
    # 負けが確定した単語を処理
    tail_lose = lose_dd.pop()
    for i in tail_dict[tail_lose]:
        result[i] = -1
        # 負け確定の単語にいける単語は勝ち確定
        tail_win = S[i][:3]
        if tail_win in tail_keys:
            # 勝ちが確定した単語を処理
            for j in tail_dict[tail_win]:
                result[j] = 1
                # 確定済みのものは削除して枝切り
                if tail_win in tail_keys:
                    tail_keys.remove(tail_win)
                # tailがこの単語のheadになっているやつは負け確定
                if S[j][:3] in tail_keys:
                    lose_dd.append(S[j][:3])
                    # 確定済みのものは削除して枝切り
                    tail_keys.remove(S[j][:3])
    
    for tail in tail_keys:
        for i in tail_dict[tail]:
            if result[i] != 1:
                break
        else:
            lose_dd.append(tail)
            if tail in tail_keys:
                tail_keys.remove(tail)


for i, s in enumerate(S):
    if result[i] == 1:
        print('Takahashi')
    elif result[i] == -1:
        print('Aoki')
    else:
        print('Draw')




