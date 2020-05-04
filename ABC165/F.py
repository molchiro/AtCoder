import bisect

N = int(input())
A = list(map(int, input().split()))
tree = [{'par': 0, 'LIS': []} for i in range(N)]
for i in range(N-1):
    u, v = list(map(int, input().split()))
    tree[v-1]['par'] = u - 1

tree[0]['LIS'] = [A[0]]
for i in range(1, N):
    a = A[i]
    par = tree[i]['par']
    LIS = tree[par]['LIS'][:]
    if a > LIS[-1]:
        LIS.append(a)
    else:
        LIS[bisect.bisect_left(LIS, a)] = a
    tree[i]['LIS'] = LIS[:]
for i in range(N):
    print(len(tree[i]['LIS']))