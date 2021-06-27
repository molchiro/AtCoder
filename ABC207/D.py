N = int(input())

S = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    S.append(a+b*1j)
T = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    T.append(a+b*1j)
# print(S)
# print(T)
S.sort(key=lambda x: (x.real, x.imag))
for _ in range(4):
    T = [x*(1j) for x in T]
    # print(T)
    tmp = T[:]
    tmp.sort(key=lambda x: (x.real, x.imag))
    diff = S[0]-tmp[0]
    tmp = [x+diff for x in tmp]
    if set(S) == set(tmp):
        print('Yes')
        exit()
print('No')