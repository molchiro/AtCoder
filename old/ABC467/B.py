N = int(input())
keep = 0

for _ in range(N):
    A, B, S = input().split()
    A, B = int(A), int(B)
    if S == 'keep':
        keep += B-A

print(keep)
