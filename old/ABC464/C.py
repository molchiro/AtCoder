from collections import Counter

N, M = list(map(int, input().split()))
birds = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

counter = Counter([a for a, _, _ in birds])
ans = len(counter.items())

events = [(d, a, b) for a, d, b in birds]
events.sort(reverse=True)

for j in range(M):
    while events and events[-1][0] <= j:
        _, a, b = events.pop()
        if counter[a] == 1:
            ans -= 1
        counter[a] -= 1

        if counter[b] == 0:
            ans += 1
        counter[b] += 1
    print(ans)