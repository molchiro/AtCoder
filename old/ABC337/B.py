H, W, K = list(map(int, input().split()))
N = (H+1)*(W+1)
ban = 2*(10**5)+1
line = [ban]*(2*N)
for h in range(H):
    ow = h*(W+1) + N
    S = input()
    for w in range(W):
        oh = w*(H+1)
        if S[w] == 'o':
            line[ow+w] = 0
            line[oh+h] = 0
        if S[w] == '.':
            line[ow+w] = 1
            line[oh+h] = 1
# print(line)
tmp = sum(line[:K])
ans = tmp
for i in range(K, 2*N):
    tmp -= line[i-K]
    tmp += line[i]
    ans = min(ans, tmp)

if ans < ban:
    print(ans)
else:
    print(-1)