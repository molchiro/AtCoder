N, A = list(map(int, input().split()))
T = list(map(int, input().split()))
t = 0
idx = 0

while idx < N:
    if t >= T[idx]:
        t += A
        idx += 1

        print(t)
    else:
        t = T[idx]