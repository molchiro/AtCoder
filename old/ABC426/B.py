S = list(input())
if S.count(S[0]) == 1:
    print(S[0])
else:
    print([s for s in S if s != S[0]][0])
