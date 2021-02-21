A, B, C = list(map(int, input().split()))
A_seen = [0]*10
A %= 10
A_ = A
A_loop_size = 0
while A_seen[A_] == 0:
    A_seen[A_] = 1
    A_loop_size += 1
    A_ *= A
    A_ %= 10

B_seen = [0]*(A_loop_size+1)
B %= A_loop_size
B_ = B
B_loop_size = 0
while B_seen[B_] == 0:
    B_seen[B_] = 1
    B_loop_size += 1
    B_ *= B
    B_ %= A_loop_size

if B_ == 1:
    BC = 1
elif B_seen[0] and C >= B_loop_size:
    BC = A_loop_size
else:
    BC = B**((C%B_loop_size)%A_loop_size)

print(A**(BC)%10)
