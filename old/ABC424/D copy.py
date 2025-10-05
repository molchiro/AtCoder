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
            for (h, w) in pattern:
                field[h][w] = 0
            
            if check(field):
                # print(candidates, i)
                for (h, w) in pattern:
                    field[h][w] = 1
                return i
            
            for (h, w) in pattern:
                field[h][w] = 1
    
    return 10**18

from itertools import combinations

for _ in range(T):
    H, W = list(map(int, input().split()))
    field = []
    for h in range(H):
        S = input()
        field.append([1 if x == '#' else 0 for x in S])
    
    candidates = [(h*2+1, w*2+1) for h in range(H//2) for w in range(W//2)]
    ans = 10**18
    for i in range(1<<(len(candidates)*2)):
        new_candidates = []
        for j in range(len(candidates)):
            h, w = candidates[j]
            dh = -1 if i>>j & 1 else 0
            dw = -1 if i>>(len(candidates)+j) & 1 else 0
            new_candidates.append((h+dh, w+dw))
            ans = min(ans, solve(field, new_candidates))

    
    print(ans)