N = int(input())
A = list(map(int, input().split()))

# 残り１、２、３枚の皿がi, j, k種類ある時に食べきるのに必要な回数をdpで求める
dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0

def mem_rec(i, j, k):
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    
    ans = 0
    if i > 0:
        ans += mem_rec(i-1, j, k)*i
    if j > 0:
        ans += mem_rec(i+1, j-1, k)*j
    if k > 0:
        ans += mem_rec(i, j+1, k-1)*k
    ans += N
    ans /= i+j+k

    dp[i][j][k] = ans
    return ans

print(mem_rec(A.count(1), A.count(2), A.count(3)))