N = int(input())
A = list(map(int, input().split()))
A_plus_i = [i + A[i] for i in range(N)]
A_minus_i = [A[i] - i for i in range(N)]
keys = [-x for x in A_minus_i if x < 0]
ans = 0
for key in keys:
    ans += A_plus_i.count(key)
print(ans)