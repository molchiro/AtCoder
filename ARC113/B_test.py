for i in range(1, 20):
    for j in range(1, 5):
        for k in range(1, 5):


            A, B, C = i, j, k
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

            ans = (A**(BC)%10)
            ans_ = (i**(j**k))%10
            if ans != ans_:
                print(i, j, k, A_loop_size, B_loop_size, BC)
                exit()

print('OK')