N, K = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))

now = 0
route = []
seen = set()
while not now in seen:
    route.append(now)
    seen.add(now)
    now = A[now]

loop_start = route.index(now)
loop_size = len(route) - loop_start

n_for_loop = min(K, loop_start)
n_in_loop = (K - n_for_loop) % loop_size

print(route[n_for_loop + n_in_loop] + 1)
