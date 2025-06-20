N = int(input())
saba = [list(map(int, input().split())) for _ in range(N)]
iwashi = [list(map(int, input().split())) for _ in range(N)]

def solve():
    global N, saba, iwashi

    # y座標ごとの魚の位置を管理
    saba_line = [[] for _ in range(10**5+1)]
    for x, y in saba:
        saba_line[y].append(x)
    for i in range(10**5+1):
        saba_line[i].sort()

    iwashi_line = [[] for _ in range(10**5+1)]
    for x, y in iwashi:
        iwashi_line[y].append(x)
    for i in range(10**5+1):
        iwashi_line[i].sort()

    res = 1
    line1 = []
    line2 = []
    ct = 1000
    min_x = 10**6
    max_x = -1
    for y in range(10**5+1):
        if len(saba_line[y]) == 0:
            continue

        last = y

        l = saba_line[y][0]
        if l >= 10**5:
            l -= 1
        
        r = saba_line[y][-1]+1
        if r > 10**5:
            r -= 1

        if l > min_x and r < max_x:
            continue

        if len(line1) == 0 and len(line2) == 0:
            line1.append((l, y))
            line2.append((r, y))
            min_x = l
            max_x = r
            ct -= 2
        else:
            if l < min_x:
                line1.append((min_x, y))
                line1.append((l, y))
                min_x = l
                ct -= 2
            
            if r > max_x:
                line2.append((max_x, y))
                line2.append((r, y))
                max_x = r
                ct -= 2
        
        if ct < 10:
            break
    
    if line1[-1][1] != last:
        line1.append((min_x, last))
    if line2[-1][1] != last:
        line2.append((max_x, last))

    return max(res, 0), line1+line2[::-1]

score, ans = solve()

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])