SA, SB = input().split()
LA, LB = len(SA), len(SB)
A, B = int(SA), int(SB)
# [上から何桁][4or9使ったフラグ][未満フラグ]
dpA = [[[0]*2 for _ in range(2)] for _ in range(LA+1)]
dpA[0][0][0] = 1
for i in range(LA):
    D = int(SA[i])
    for j in range(2):
        for k in range(2):
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k
                if k == 0 and d > D:
                    continue
                if d in [4, 9]:
                    nj = 1
                if d < D:
                    nk = 1
                dpA[ni][nj][nk] += dpA[i][j][k]
dpB = [[[0]*2 for _ in range(2)] for _ in range(LB+1)]
dpB[0][0][0] = 1
for i in range(LB):
    D = int(SB[i])
    for j in range(2):
        for k in range(2):
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k
                if k == 0 and d > D:
                    continue
                if d in [4, 9]:
                    nj = 1
                if d < D:
                    nk = 1
                dpB[ni][nj][nk] += dpB[i][j][k]
print(dpB[LB][1][0]+dpB[LB][1][1]-dpA[LA][1][1])