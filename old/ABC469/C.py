N = int(input())
S = input()

S = list(S)[::-1]
# print(S)
ans = []

ct = 0
accum = 0
for i in range(1, N+1):
    while S and ct < i:
        s = S.pop()
        accum += 1
        if s == 'o':
            continue
        else:
            ct += 1
    ans.append(accum)
    # print(S)

print(*ans, sep='\n')