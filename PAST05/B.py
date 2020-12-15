N = int(input())
S = input()
T = []
for s in S:
    T = [x for x in T if x != s]
    T.append(s)
print(''.join(T))