N, K = list(map(int, input().split()))
parts = [[] for _ in range(10)]
M = (-1, '')
for _ in range(N):
    S = input()
    parts[len(S)].append(S)
    if int(S) > M[0]:
        M = (int(S), S)

for i in range(10):
    parts[i].sort(key=lambda x: int(x))

# 左端を選んだ後は貪欲でいい

# 0から始まってない数字から始めるとき
# 0から始まっている数字から始める時