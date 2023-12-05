N = int(input())

for i in range(2**N):
    S = format(i, f'0{N}b')
    tmp = 0
    for s in S:
        if s == '0':
            tmp += 1
        else:
            tmp -= 1
        
        if tmp < 0:
            break
    else:
        if tmp == 0:
            print(''.join(['(' if s == '0' else ')' for s in S]))