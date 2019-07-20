N = int(input())
A = list(map(int, input().split()))

res = [0 for i in range(N)]
for i in range(N, 0, -1):
    othors_idxs = [(j+1)*i-1 for j in range(int(N/i)) if j != 0]
    othors = [res[idx] for idx in othors_idxs]
    if sum(othors + [1]) % 2 == A[i-1]:
        res[i-1] = 1

ans = [str(i+1) for i in range(N) if res[i] == 1]
l = len(ans)
if l > 0:
    print(l)
    print(' '.join(ans))
else:
    print(0)
    