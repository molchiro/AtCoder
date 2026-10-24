S = input()
# S = "a"*10000
N = len(S)

zeros = []
ones = []

ans = 0

# 初期処理
for i in range(N):
    zeros.append((i, i))

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        zeros.append((i, i+1))
    else:
        ones.append((i, i+1))

ans += len(ones) + len(zeros)

while zeros or ones:
    n_zeros = []
    n_ones = []

    for (l, r) in zeros:
        l -= 1
        r += 1
        if l < 0:
            continue
        if r >= N:
            continue

        if S[l] == S[r]:
            n_zeros.append((l, r))
        else:
            n_ones.append((l, r))
    
    for (l, r) in ones:
        l -= 1
        r += 1
        if l < 0:
            continue
        if r >= N:
            continue

        if S[l] == S[r]:
            n_ones.append((l, r))

    zeros = n_zeros
    ones = n_ones

    ans += len(ones) + len(zeros)

print(ans)