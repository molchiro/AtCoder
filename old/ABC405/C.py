N = int(input())
A = list(map(int, input().split()))

cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)

ans = 0

for i, a in enumerate(A):
    ans += (cumsum[-1] - cumsum[i+1])*a

print(ans)