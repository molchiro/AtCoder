from collections import Counter

N = int(input())
K = []
A = []
for _ in range(N):
    dice = list(map(int, input().split()))
    K.append(dice[0])
    A.append(Counter(dice[1:]))

# print(*K)
# print(*A, sep='\n')

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        tmp = 0
        for k_i, v_i in A[i].items():
            # print(k_i, v_i)
            tmp += v_i/K[i] * A[j][k_i]/K[j]
        # print(tmp)
        ans = max(ans, tmp)

print(ans)