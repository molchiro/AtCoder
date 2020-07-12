N = int(input())
d = {i+1: 0 for i in range(N)}
for i in range(1, int(N**0.5)):
    for j in range(1, i+1):
        for k in range(1, j+1):
            n = i**2 + j**2 + k**2 + i*j + j*k + k*i
            if n > N:
                continue
            if len(set([i, j, k])) == 1:
                d[n] +=  1
            elif len(set([i, j, k])) == 2:
                d[n] +=  3
            else:
                d[n] +=  6
for i in range(N):
    print(d[i+1])