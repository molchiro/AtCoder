from collections import defaultdict
N, M = list(map(int, input().split()))
S_list = [input() for _ in range(N)]
T_list = [input() for _ in range(M)]
T_dict = defaultdict(set)
for t in T_list:
    T_dict[len(t)].add(t)

def dfs(parts, current='', rem=16-len('_'.join(S_list))):
    # 増やせる文字数を超えていたら失敗
    if rem < 0:
        return
    # 全部品を使いきっていれば判定
    if parts == []:
        n = len(current)
        if 3 <= n <= 16 and current not in T_dict[n]:
            print(current)
            exit()
        return
    if current != '':
        # print('_', current)
        dfs(parts, current+'_', rem-1)
    for p in parts:
        # print('p', p, current)
        dfs([x for x in parts if x != p], current+'_'+p if current else p, rem)

dfs(S_list)

print(-1)