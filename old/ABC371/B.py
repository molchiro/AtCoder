N, M = list(map(int, input().split()))
seen = [0]*N
for _ in range(M):
    A, B = input().split()
    if B == 'F':
        print('No')
    else:
        a = int(A)-1
        if seen[a]:
            print('No')
        else:
            print('Yes')
            seen[a] = 1