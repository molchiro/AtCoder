N, S = input().split()
N = int(N)
el_Count = [[0, 0, 0, 0] for _ in range(N+1)]
for i in range(N):
    el_Count[i+1][0] = el_Count[i][0] + (1 if S[i] == 'A' else 0)
    el_Count[i+1][1] = el_Count[i][1] + (1 if S[i] == 'T' else 0)
    el_Count[i+1][2] = el_Count[i][2] + (1 if S[i] == 'C' else 0)
    el_Count[i+1][3] = el_Count[i][3] + (1 if S[i] == 'G' else 0)
ans = 0
for i in range(N-1):
    for j in range(i+2, N+1, 2):
        len_A = el_Count[j][0] - el_Count[i][0]
        len_T = el_Count[j][1] - el_Count[i][1]
        len_G = el_Count[j][2] - el_Count[i][2]
        len_C = el_Count[j][3] - el_Count[i][3]
        if len_A == len_T and len_G == len_C:
            ans += 1
print(ans)
