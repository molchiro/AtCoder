N, K = list(map(int, input().split()))
S = input()

prev = S[0]
n = 1

l = []

for i in range(1, N):
    if S[i] == prev:
        n += 1
    else:
        l.append((prev, n))
        prev = S[i]
        n = 1

l.append((prev, n))

# print(l)

n = 0
for i in range(len(l)):
    if l[i][0] == '1':
        n += 1

    if n >= K:
        l[i], l[i-1] = l[i-1], l[i]
        break

# print(l)

print(*[c*n for c, n in l], sep='')