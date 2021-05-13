N = int(input())
S = list(input())
Q = int(input())
is_fliped = 0
for _ in range(Q):
    T, A, B = [x-1 for x in map(int, input().split())]
    if T == 0:
        if is_fliped:
            A = (A+N)%(2*N)
            B = (B+N)%(2*N)
        S[A], S[B] = S[B], S[A]
    else:
        is_fliped ^= 1
if is_fliped:
    S = S[N:] + S[:N]
print(''.join(S))