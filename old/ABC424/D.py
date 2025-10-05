T = int(input())

def check(field):
    H = len(field)
    W = len(field[0])
    for h in range(H-1):
        for w in range(W-1):
            if field[h][w] + field[h+1][w] + field[h][w+1] + field[h+1][w+1] == 4:
                return False
    
    return True

def solve(field, candidates):
    # print(candidates)
    for i in range(10):
        for pattern in combinations(candidates, i):
            # print(pattern)
            for (h, w) in pattern:
                field[h][w] = 0

            # print(*field, sep='\n')
            
            if check(field):
                return i
            
            for (h, w) in pattern:
                field[h][w] = 1

from itertools import combinations

for _ in range(T):
    H, W = list(map(int, input().split()))
    field = []
    for h in range(H):
        S = input()
        field.append([1 if x == '#' else 0 for x in S])
    # print(*field, sep='\n')
    candidates = [(h, w) for h in range(1, H-1) for w in range(1, W-1)]
    candidates = [(h, w) for h, w in candidates if field[h][w]]
    
    print(solve(field, candidates))
