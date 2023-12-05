N, D, P = list(map(int, input().split()))
F = list(map(int, input().split()))
F.sort(reverse=True)
F += [0]*((D-N%D)%D)
# print(F)
ans = 0
for i in range(len(F)//D):
    ans += min(sum(F[i*D:(i+1)*D]), P)
print(ans)