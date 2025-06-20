T = input()
U = input()
for i in range(len(T)-len(U)+1):
    f = 1

    for j in range(len(U)):
        # print(T[i+j], U[j])
        if T[i+j] == '?' or T[i+j] == U[j]:
            continue

        f = 0

    if f:
        print('Yes')
        break
else:
    print('No')