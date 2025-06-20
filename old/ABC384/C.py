A = list(map(int, input().split()))

ans = []
for i in range(1, 1<<5):
    name = ''
    score = 0
    for j in range(5):
        if i >> j & 1:
            name += chr(ord('A')+j)
            score += A[j]
    ans.append((score, name))


for score, name in sorted(ans, key=lambda x: (-x[0], x[1])):
    print(name)