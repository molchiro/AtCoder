def children(N, u, d):
    if d < 0:
        return 0
    left = u
    right = u
    for _ in range(d):
        left += left
        right += right+1
        if left > N:
            break
    return max(0, min(right, N) - left + 1)

def culc(N, X, K):
    if K == 0:
        return 1
    ans = children(N, X, K)
    if X > 1:
        ans += culc(N, X//2, K-1) - children(N, X, K-2)
    return ans

T = int(input())
for _ in range(T):
    N, X, K = list(map(int, input().split()))
    print(culc(N, X, K))