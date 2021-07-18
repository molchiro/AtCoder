N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
i_A = 0
i_B = 0
i_C = 0
while i_A < N and i_B < N and i_C < N:
    Ai = A[i_A]
    while Ai >= B[i_B]:
        i_B += 1
        if i_B >= N:
            print(ans)
            exit()
    Bi = B[i_B]
    while Bi >= C[i_C]:
        i_C += 1
        if i_C >= N:
            print(ans)
            exit()
    ans += 1
    i_A += 1
    i_B += 1
    i_C += 1
print(ans)