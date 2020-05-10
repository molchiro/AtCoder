N, K = list(map(int, input().split()))
K -= 1
A = list(map(lambda x: int(x) - 1, input().split()))
seen = [None]*N
seen_set = set()
now = 0
for i in range(N):
    seen[i] = now
    seen_set.add(now)
    to = A[now]
    now = to
    if now in seen_set:
        seen[i+1] = now
        loop_s = seen.index(now)
        loop_end = i + 1
        size = loop_end - loop_s
        break
if K <= loop_s:
    print(seen[K+1] + 1)
else:
    K -= loop_s
    print(seen[loop_s + 1 + K % size] + 1)