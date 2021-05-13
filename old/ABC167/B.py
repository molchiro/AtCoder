A, B ,C, K = list(map(int, input().split()))

A_ = min(A, K)
K -= A_
B_ = min(B, K)
K -= B_
C_ = min(C, K)

print(A_ * 1 + B_ * 0 + C_ * -1)
