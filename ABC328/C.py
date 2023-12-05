N, Q = list(map(int, input().split()))
S = input()
cumsum = []
prev = ''
now = 0
for s in S:
    if s == prev:
        now += 1
    prev = s
    cumsum.append(now)
# print(cumsum)
for _ in range(Q):
    l, r = list(map(lambda x: int(x) - 1, input().split()))
    print(cumsum[r]-cumsum[l])