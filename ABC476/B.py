N = int(input())
S = input()
T = input()

f = 1
for i in range(N):
    if T[i] == S[i]:
        continue

    if T[i] == '*':
        continue

    f = 0

print('Yes' if f else 'No')