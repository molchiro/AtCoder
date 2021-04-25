N = int(input())
S = input()
Q = int(input())
order = [i for i in range(2*N)]
is_fliped = 0
for _ in range(Q):
    T, A, B = list(map(lambda x: int(x) - 1, input().split()))
    if T == 0:
        if is_fliped:
            if B < N:
                order[A+N], order[B+N] = order[B+N], order[A+N]
            elif A >= N:
                order[A-N], order[B-N] = order[B-N], order[A-N]
            else:
                order[A+N], order[B-N] = order[B-N], order[A+N]
        else:
            order[A], order[B] = order[B], order[A]
    else:
        is_fliped = 1-is_fliped
if is_fliped:
    order = order[N:] + order[:N]
ans = ''.join([S[i] for i in order])
print(ans)