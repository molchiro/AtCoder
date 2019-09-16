N = int(input())
INPUT = list(map(int, input().split()))
POSs = []
NEGs = []
for e in INPUT:
    if e > 0:
        POSs.append(e)
    else:
        NEGs.append(e)

res = []
for i in range(N-2):
    if len(NEGs) == 0:
        pos_min = min(POSs)
        pos_max = max(POSs)
        POSs.remove(pos_min)
        POSs.remove(pos_max)
        res.append([pos_min, pos_max])
        new_val = pos_min - pos_max
    elif len(POSs) == 0:
        neg_min = min(NEGs)
        neg_max = max(NEGs)
        NEGs.remove(neg_min)
        NEGs.remove(neg_max)
        res.append([neg_max, neg_min])
        new_val = neg_max - neg_min
    elif len(POSs) > 1:
        pos_min = min(POSs)
        POSs.remove(pos_min)
        neg = NEGs.pop()
        res.append([neg, pos_min])
        new_val = neg - pos_min
    else:
        pos = POSs.pop()
        neg = NEGs.pop()
        res.append([pos, neg])
        new_val = pos - neg

    if new_val < 0:
        NEGs.append(new_val)
    else:
        POSs.append(new_val)

last_pair = POSs + NEGs
M = max(last_pair)
m = min(last_pair)
res.append([M, m])
print(M - m)
for el in res:
    print(el[0], el[1])
