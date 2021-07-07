N, M = list(map(int, input().split()))
# d[i][j] = iからjへの最短経路
# k=1~Nで更新しながら使う
d = [[0]*N for _ in range(N)]
# k番目の都市まで通って良い時の合計
# k=1~Nで更新しながら使う
total_d = 0
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    d[A-1][B-1] = C
    total_d += C

ans = 0
for k in range(N):
    for i in range(N):
        if i == k:
            continue
        i_to_k = d[i][k]
        if i_to_k == 0:
            continue
        for j in range(N):
            if i == j:
                continue
            current_d = d[i][j]
            k_to_j = d[k][j]
            if k_to_j == 0:
                continue
            if current_d == 0 and k_to_j > 0:
                d[i][j] = i_to_k + k_to_j
                total_d += i_to_k + k_to_j
            elif i_to_k + k_to_j < current_d:
                d[i][j] = i_to_k + k_to_j
                total_d -= current_d - (i_to_k + k_to_j)
    ans += total_d
    # print(*d, sep='\n')
    # print(ans)

print(ans)