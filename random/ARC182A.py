mod = 998244353

N, Q = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

act = [(-1, 1) for _ in range(Q)]

for i in range(Q-1):
    pi, vi = queries[i]
    for j in range(i+1, Q):
        pj, vj = queries[j]
        if vi <= vj:
            continue
        
        if pi == pj:
            print(0)
            exit()
        elif pi < pj:
            if -1 in act[i]:
                act[i] = (-1,)
            else:
                print(0)
                exit()
            if 1 in act[j]:
                act[j] = (1,)
            else:
                print(0)
                exit()
        else:
            if 1 in act[i]:
                act[i] = (1,)
            else:
                print(0)
                exit()
            if -1 in act[j]:
                act[j] = (-1,)
            else:
                print(0)
                exit()

ct = act.count((-1, 1))
print(pow(2, ct, mod))