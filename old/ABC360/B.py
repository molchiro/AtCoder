S, T = input().split()

for w in range(1, len(S)):
    for c in range(w):
        t = ''.join([S[i] for i in range(c, len(S), w)])
        # print(t)
        if t == T:
            print('Yes')
            exit()
print('No')
