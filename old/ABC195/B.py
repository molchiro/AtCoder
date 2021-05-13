A, B, W = list(map(int, input().split()))
W *= 1000
i = 1
m = float('inf')
M = -1
while A <= W/i:
    if W/i <= B:
        m = min(m, i)
        M = max(M, i)
    i += 1

if m == float('inf'):
    print('UNSATISFIABLE')
else:
    print(m, M)