H, W, M = list(map(int, input().split()))

targets = set()
row = [0]*H
col = [0]*W

for _ in range(M):
    h, w = list(map(lambda x: int(x) - 1, input().split()))
    row[h] += 1
    col[w] += 1
    targets.add((h, w))

r_max = max(row)
c_max = max(col)
ans = 0

maxed_h = set([h for h in range(H) if row[h] == r_max])
maxed_w = set([w for w in range(W) if col[w] == c_max])
bomb_option_sites_n = len(maxed_h)*len(maxed_w)
targets_on_bomb_option = 0
for th, tw in targets:
    if th in maxed_h and tw in maxed_w:
        targets_on_bomb_option += 1

if bomb_option_sites_n == targets_on_bomb_option:
    print(r_max + c_max - 1)
else:
    print(r_max + c_max)
