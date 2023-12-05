N = int(input())
S = input()
pos = [2*10**5]*2
seen = set([pos[0]*10**6+pos[1]])
for s in S:
    dx, dy = [(0, 1), (1, 0), (-1, 0), (0, -1)]['URLD'.index(s)]
    pos[0] += dx
    pos[1] += dy
    seen.add(pos[0]*10**6+pos[1])
    # print(pos)
    # print(seen)
print('Yes' if len(seen) < N+1 else 'No')