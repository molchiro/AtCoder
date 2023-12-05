N, K, P = list(map(int, input().split()))
dp = [float('inf')]*(int(str(P)*K)+1)
dp[0] = 0
# print(int(str(P)*K))
for _ in range(N):
    C, *A = list(map(int, input().split()))
    # print(C, A)
    # input()
    for i in range(int(str(P)*K), -1, -1):
        idx_str = '00000'+str(i)
        idx_str = idx_str[::-1]
        idx_str = idx_str[:K]
        idx_str = idx_str[::-1]
        idx_list = list(list(map(int, list(idx_str))))
        # print(i, idx_str, idx_list)
        # input()
        for k in range(K):
            idx_list[k] = min(idx_list[k]+A[k], P)
        new_idx = int(''.join(map(str, idx_list)))
        # print(new_idx)
        # input()
        dp[new_idx] = min(dp[new_idx], dp[i]+C)
    # debug
#     for i in range(int(str(P)*K)+1):
#         if dp[i] != float('inf'):
#             print(i, dp[i])
#     input()
# print(dp)
ans = dp[-1]
if ans == float('inf'):
    print(-1)
else:
    print(ans)