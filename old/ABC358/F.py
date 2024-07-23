N, M, K = list(map(int, input().split()))

if  N > K:
    print('No')
    exit()

if (K-N)%2:
    print('No')
    exit()

if N*M < K:
    print('No')
    exit()

print('Yes')
ans = ['++'*(M-1)+'+S+']
for _ in range(N):
    ans.append('+'+'|'.join(['o']*M)+'+')
    ans.append('+'+'+'.join(['-']*(M-1))+'+.+')
ans.pop()
ans.append('++'*(M-1)+'+G+')
ans = [list(x) for x in ans]

k = N
if N%2:
    # くりかえす
    # +++++S+
    # +o.o.o+
    # +.+-+-+
    # +o.o.o+
    # +-+-+.+
    for i in range(N//2):
        for j in range(M-1):
            if k < K:
                h = 2+i*4
                w = 2*M-j*2-1
                ans[h][w] = '-'
                ans[h-1][w-1] = '.'
                ans[h+1][w-1] = '.'
                ans[h][w-2] = '.'
        
    

    pass

    # くねくねさせる

else:
        for j in range(M-1):
            if k < K:
                h = 2+i*4
                w = 2*M-j*2-1
                ans[h][w] = '-'
                ans[h-1][w-1] = '.'
                ans[h+1][w-1] = '.'
                ans[h][w-2] = '.'
ans = [''.join(x) for x in ans]
print(*ans, sep='\n')