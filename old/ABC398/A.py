N = int(input())
ans = ['-']*N
ans[(N-1)//2] = '='
ans[-(-N)//2] = '='
print(''.join(ans))