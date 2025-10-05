N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = sum([min(a, b) for a, b in zip(A, B)])

for _ in range(Q):
    c, X, V = input().split()
    X = int(X)-1
    V = int(V)
    old_a = A[X]
    old_b = B[X]
    if c == 'A':
        A[X] = V
    else:
        B[X] = V
    new_a = A[X]
    new_b = B[X]
    ans += min(new_a, new_b) - min(old_a, old_b)
    print(ans)