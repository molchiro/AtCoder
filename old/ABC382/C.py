N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_w_i = [(b, i) for i, b in enumerate(B)]
B_w_i.sort()

ans = [-1]*M

for i, a in enumerate(A):
    while B_w_i and B_w_i[-1][0] >= a:
        b, j = B_w_i.pop()
        ans[j] = i+1

print(*ans, sep='\n')