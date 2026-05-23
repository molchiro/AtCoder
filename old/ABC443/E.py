T = int(input())
for _ in range(T):
    N, C = list(map(int, input().split()))

    field = [input() for _ in range(N)]
    dp1 = [0]*N # あるCにいられるか
    dp1[C-1] = 1
    dp2 = [0 if s == '#' else 1 for s in field.pop()] # あるCについて下が全てあ空きマスの状態をキープできるか
    while field:
        row = field.pop()

        ndp1 = [0]*N
        ndp2 = [int(dp2[c] and row[c] == '.') for c in range(N)]
        
        for c in range(N):
            if not dp1[c]:
                continue

            for d in [-1, 0, 1]:
                new_c = c+d
                if not 0 <= new_c < N:
                    continue

                if row[new_c] == '#':
                    if dp2[new_c]:
                        ndp1[new_c] = 1
                        if dp2[new_c]:
                            ndp2[new_c] = 1
                else:
                    ndp1[new_c] = 1
                    if dp2[new_c]:
                        ndp2[new_c] = 1
        dp1 = ndp1
        dp2 = ndp2
    
    print(''.join([str(e) for e in dp1]))

