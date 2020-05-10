N, K = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))

now = 0
seen = []
while True:
    seen.append(now)
    teleporter = A[now]
    A[now] = 'used'
    if teleporter == 'used':
        break
    else:
        now = teleporter  

loop_s = seen.index(now)
size = len(seen) - loop_s - 1

if K <= loop_s:
    print(seen[K] + 1)
else:
    print(seen[loop_s +(K - loop_s) % size] + 1)