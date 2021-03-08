N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
min_AB = min([A+B for A, B in AB])
AB = [[A, B] for A, B in AB if A < min_AB or B < min_AB]
N = len(AB)
# print(min_AB)
if N == 1:
    print(min_AB)
else:
    AB.sort(key=lambda x: x[1])
    B_min = AB[0][1]
    B_min2 = AB[1][1]
    AB.sort(key=lambda x: x[0])
    A_min = AB[0][0]
    A_min2 = AB[1][0]
    if [B for A, B in AB[::-1]].index(B_min) < N-1:
        print(max(A_min, B_min))
    else:
        print(min(max(A_min, B_min2), max(A_min2, B_min)))