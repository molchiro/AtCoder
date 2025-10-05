N = int(input())
S = [input() for _ in range(N)]
s = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        s.add(S[i]+S[j])
print(len(s))