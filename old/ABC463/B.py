N, X = input().split()
N = int(N)
seki = [N]*5
for _ in range(N):
    S = input()
    for i in range(5):
        if S[i] == 'x':
            seki[i] -= 1
idx = ord(X) - ord('A')
# print(seki)
print('Yes' if seki[idx] > 0 else 'No')
