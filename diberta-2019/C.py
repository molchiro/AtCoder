N = int(input())

AB_cnt = 0
A_cnt = 0
B_cnt = 0
for i in range(N):
    S = input()
    for j in range(len(S)-1):
        if S[j:j+2] == 'AB':
            AB_cnt += 1
    if S[-1] == 'A':
        A_cnt += 1
    if S[0] == 'B':
        B_cnt += 1

print(AB_cnt + min(A_cnt, B_cnt))