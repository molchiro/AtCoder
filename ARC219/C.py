H, W = list(map(int, input().split()))
N = int(input())
doors = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

from collections import defaultdict

dd = defaultdict(list)
for h, w in doors:
    dd[h].append(w)

doors = []
for k in dd.keys():
    doors.append(sorted(dd[k]))

# まずWのエレベータを使わないパターンを計算
ans1 = 0
for row in doors:
    ans1 += 2*row[-1]

# Wを使うパターン
both = []
for row in doors:
    row_ = [0] + row[:] + [W-1]
    tmp = 10**18
    for i in range(len(row)+1):
        l = row_[i]
        r = row_[i+1]
        tmp = min(tmp, 2*l + 2*(W-1-r))
    both.append(tmp)


ans2 = 10**18
if len(doors) >= 2:
    both.sort()
    ans2 = sum(both)

    tmp = both.pop() - (W-1)
    tmp += both.pop() - (W-1)
    ans2 -= tmp

    while len(both) >= 2 and both[-1]+both[-2] - 2*(W-1) > 0:
        tmp = both.pop() - (W-1)
        tmp += both.pop() - (W-1)
        ans2 -= tmp

print(min(ans1, ans2))